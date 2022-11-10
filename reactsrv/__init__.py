
""" This module serves frontend static files, intended for react based projects """

import os
from flask import Blueprint

from . import urls


def init(app, react_folder='build'):
    """
    Initiates this app and attaches it to the flask instance passed.
    """
    blueprint = Blueprint(
        name="reactsrv", import_name='reactsrv',
        template_folder=os.path.join(app.root_path, react_folder),
        static_folder=os.path.join(app.root_path, react_folder, 'static')
    )

    urls.add_urls(blueprint)

    app.register_blueprint(blueprint)
