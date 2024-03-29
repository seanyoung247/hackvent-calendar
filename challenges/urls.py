"""
Defines the url routes managed by this module
"""
from . import views


def url_rules():
    """ Defines the url routes served by this module """
    return [
        {'rule': '/challenge', 'view': views.Challenge.as_view('challenge')},
    ]
