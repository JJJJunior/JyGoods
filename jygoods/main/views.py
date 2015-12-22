# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""
from flask import render_template
from jygoods.main import main
from jygoods.main.forms import TestForm


@main.route('/')
def index():
    form = TestForm()
    return render_template('main/base.html', form=form)


