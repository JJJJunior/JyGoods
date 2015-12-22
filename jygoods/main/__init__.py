# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from jygoods.main import views

