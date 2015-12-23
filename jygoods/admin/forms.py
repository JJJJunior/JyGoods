# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[Required(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[Required(), Length(1, 64)])
    submit = SubmitField(u'提交')