"""
Defines the url routes managed by this app
"""
from . import views


def add_urls(bp):
    
    bp.add_url_rule(rule='/challenge', view_func=views.Challenge.as_view('challenge'))

