# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask.ext.wtf import Form
from wtforms import SelectField


class TestForm(Form):
    a = ['a', 'b', 'c', 'd']
