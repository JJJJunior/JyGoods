# *-*coding: utf-8 *-*

"""
author : JuniorSean
"""

from flask import Blueprint


admin = Blueprint('admin', __name__)

from jygoods.admin import views