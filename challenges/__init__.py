
"""
This module provides server routes for code challenges
"""

import os
from flask import Blueprint

from . import urls


def init(app):
    """
    Initiates this app and attaches it to the flask instance passed.
    """
    blueprint = Blueprint(
        name="challenges", import_name='challenges'
    )

    urls.add_urls(blueprint)

    app.register_blueprint(blueprint)
    