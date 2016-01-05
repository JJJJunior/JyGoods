# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from jygoods.admin.models import db
from jygoods.admin.models import Permission
from jygoods.admin.models import Role, User
import forgery_py
import random


def init_db():
    db.drop_all()
    db.create_all()
    roles = {
        'User': (Permission.QUERY_PRODUCT, True),
        'Manager': (Permission.QUERY_PRODUCT |
                    Permission.DELETE_PRODUCT |
                    Permission.ADD_PRODUCT, False),
        'Administrator': (0xff, False)
    }
    for r in roles:
        role = Role.query.filter_by(name=r).first()
        if role is None:
            role = Role(name=r)
        role.permissions = roles[r][0]
        role.default = roles[r][1]
        db.session.add(role)
        try:
            db.session.commit()
        except:
            db.session.rollback()


def create_user(count):
    for x in xrange(0, count):
        u = User()
        u.email = forgery_py.internet.email_address()
        u.password(forgery_py.name.company_name())
        u.role_id = random.choice(Role.query.all()).id
        db.session.add(u)
        try:
            db.session.commit()
        except:
            db.session.rollback()
