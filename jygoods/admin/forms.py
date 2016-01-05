# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from jygoods.admin.models import User


class LoginForm(Form):
    email = StringField(u'邮箱', validators=[Email(), DataRequired(), Length(1, 64)])
    password = PasswordField(u'密码', validators=[DataRequired(), Length(1, 64)])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'提交')


class RegisterForm(Form):
    email = StringField(u'邮箱', validators=[Email(), DataRequired(), Length(1, 64)])
    password = PasswordField(u'新密码', validators=[DataRequired(),
                                                 Length(1, 64),
                                                 EqualTo('confirm', message=u'两次输入密码不匹配')])
    confirm = PasswordField(u'确认密码')

    submit = SubmitField(u'提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已存在')


class EditUserForm(Form):
    email = StringField(u'邮箱', validators=[Email(), DataRequired(), Length(1, 64)])
    password = PasswordField(u'新密码')
    role = SelectField(u'角色', coerce=int)
    submit = SubmitField(u'提交')
