# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from jygoods import db, create_app
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
import jygoods.admin.models #导入models否则无法使用db.create_all()
from jygoods.admin.models import  User, Role
from sql import init_db


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, init_db=init_db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()