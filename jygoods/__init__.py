# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from config import my_config
from flask.ext.login import LoginManager



db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'admin.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(my_config[config_name]) #app对象加载config文件的定义
    my_config[config_name].init_app(app) #初始化app配置

    #初始化flask-sqlalchemy
    db.init_app(app)
    #初始化flask-bootstrap
    bootstrap.init_app(app)
    #初始化flask-login
    login_manager.init_app(app)

    #注册main蓝图
    from jygoods.main import main as view_main_blueprint

    app.register_blueprint(view_main_blueprint)
    #注册admin蓝图
    from jygoods.admin import admin as view_admin_blueprint

    app.register_blueprint(view_admin_blueprint, url_prefix='/admin')

    return app