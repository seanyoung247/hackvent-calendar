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
        name="{{module_name}}", import_name="{{module_name}}"
    )

    url_list = urls.url_rules()
    for url in url_list:
        blueprint.add_url_rule(rule=url['rule'], view_func=url['view'])

    app.register_blueprint(blueprint)
    