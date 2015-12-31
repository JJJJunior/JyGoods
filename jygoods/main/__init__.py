# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask import Blueprint

main = Blueprint('main', __name__, static_folder='main/static')

from jygoods.main import views

