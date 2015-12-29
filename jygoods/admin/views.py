# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from jygoods.admin import admin
from flask import render_template, redirect, request, url_for, flash
from jygoods.admin.forms import LoginForm
from flask.ext.login import login_required, login_user, current_user
from jygoods.admin.models import User


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('admin.manager'))
        flash(u'用户名或密码错误')
    return render_template('admin/login.html', form=form)


@admin.route('/manager')
@login_required
def manager():
    return 'test'