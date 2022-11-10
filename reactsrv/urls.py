"""
Defines the url routes managed by this module
"""
from . import views


def add_urls(blueprint):
    """ Defines the url routes served by this module """
    blueprint.add_url_rule(rule='/', view_func=views.index)
