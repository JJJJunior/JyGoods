# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from jygoods import db
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from jygoods import login_manager


class Permission:
    QUERY_PRODUCT = 0x01
    ADD_PRODUCT = 0x02
    DELETE_PRODUCT = 0x03
    ADMINISTER = 0x80


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    status = db.Column(db.Integer)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self):
        pass


#login加载用户回调
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True, nullable=False)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
