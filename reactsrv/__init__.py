import os
from . import urls

from flask import Blueprint


def init(app, react_folder='build'):
    """
    Initiates this app and attaches it to the flask instance passed.
    """
    bp = Blueprint( 
        name="reactsrv", import_name='reactsrv', 
        template_folder=os.path.join(app.root_path, react_folder),
        static_folder=os.path.join(app.root_path, react_folder, 'static')
    )

    urls.add_urls(bp)

    app.register_blueprint(bp)