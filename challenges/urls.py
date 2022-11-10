"""
Defines the url routes managed by this module
"""
from . import views


def add_urls(blueprint):
    """ Defines the url routes served by this module """
    blueprint.add_url_rule(rule='/challenge', view_func=views.Challenge.as_view('challenge'))
