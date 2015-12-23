# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from jygoods.admin import admin
from flask import render_template, redirect, url_for
from jygoods.admin.forms import LoginForm




@admin.route('/', methods=['GET', 'POST'])
@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print form.email.data
        print form.password.data
        return redirect(url_for('admin.login'))
    return render_template('admin/login.html', form=form)