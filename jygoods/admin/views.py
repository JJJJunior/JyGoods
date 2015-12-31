# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from jygoods.admin import admin
from flask import render_template, redirect, request, url_for, flash
from jygoods.admin.forms import LoginForm, RegisterForm
from flask.ext.login import login_user, login_required, logout_user
from jygoods.admin.models import User
from jygoods import db
from jygoods.admin.decorators import admin_required


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('admin.index'))
        flash(u'用户名或密码错误')
        return redirect(url_for('admin.login'))
    return render_template('admin/login.html', form=form)


@admin.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User()
        u.password(form.password.data)
        u.email = form.email.data
        db.session.add(u)
        try:
            db.session.commit()
            login_user(u)
            return redirect(url_for('admin.index'))
        except:
            db.session.rollback()
            flash(u'网络原因提交失败，请重试。')
            return redirect(url_for('admin.register'))
    return render_template('admin/register.html', form=form)


@admin.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('admin.index'))


@admin.route('/index')
@login_required
@admin_required
def index():
    return u'欢迎你'
