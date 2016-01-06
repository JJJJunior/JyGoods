# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from jygoods.admin import admin
from flask import render_template, redirect, request, url_for, flash
from jygoods.admin.forms import LoginForm, RegisterForm, EditUserForm
from flask.ext.login import login_user, login_required, logout_user, current_user
from jygoods.admin.models import User, Role
from jygoods import db
from jygoods.admin.decorators import admin_required
from jygoods import csrf


@csrf.error_handler
def csrf_error(reason):
    return render_template('csrf_error.html', reason=reason), 400


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('admin.manager'))
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
            return redirect(url_for('admin.manager'))
        except:
            db.session.rollback()
            flash(u'网络原因提交失败，请重试。')
            return redirect(url_for('admin.register'))
    return render_template('admin/register.html', form=form)


@admin.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('admin.manager'))


@admin.route('/manager')
@login_required
@admin_required
def manager():
    page = request.args.get('page', 1, type=int)
    pagination = User.query.paginate(page, per_page=20, error_out=False)
    users = pagination.items
    return render_template('admin/manager.html', users=users, pagination=pagination, page=page)


@admin.route('/delete_user/<int:id>')
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    page = request.args.get('page')
    if current_user.id == user.id:
        flash(u'无法删除当前用户')
    else:
        db.session.delete(user)
        try:
            db.session.commit()
            flash(u'已经删除用户')
        except:
            db.session.rollback()
            raise
    return redirect(url_for('admin.manager', page=page))


@admin.route('/edit_user/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit_user(id):
    form = EditUserForm()
    user = User.query.get_or_404(id)
    form.role.choices = [(a.id, a.name) for a in Role.query.order_by('id')]
    page = request.args.get('page', 1, type=int)
    if form.validate_on_submit():
        user.email = form.email.data
        user.password(form.password.data)
        user.role_id = form.role.data
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        flash(u'已经修改了{email}用户的信息'.format(email=user.email))
        return redirect(url_for('admin.manager', page=page))
    form.email.data = user.email
    form.role.data = user.role_id
    return render_template('admin/edit_user.html', form=form)


@csrf.exempt
@admin.route('/delete_users', methods=['GET', 'POST'])
@admin_required
def delete_users():
    page = request.args.get('page', 1, type=int)
    if request.method == "POST":
        # 去掉csrf
        for id in request.form:
            if current_user.id != id and id != 'csrf_token':
                u = User.query.get(id)
                db.session.delete(u)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
    return redirect(url_for('admin.manager', page=page))
