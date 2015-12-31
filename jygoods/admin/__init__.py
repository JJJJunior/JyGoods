# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask import Blueprint


admin = Blueprint('admin', __name__, static_folder='static')

from jygoods.admin import views