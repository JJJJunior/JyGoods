# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import my_config




db = SQLAlchemy()




def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(my_config[config_name]) #app对象加载config文件的定义
    my_config[config_name].init_app(app) #初始化app配置

    db.init_app(app)

    return app