
import os
from . import urls

from flask import Blueprint


def init(app):
    """
    Initiates this app and attaches it to the flask instance passed.
    """
    bp = Blueprint( 
        name="challenges", import_name='challenges'
    )

    urls.add_urls(bp)

    app.register_blueprint(bp)
    