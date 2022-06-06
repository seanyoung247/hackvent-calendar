"""
Defines the url routes managed by this app
"""
from . import views


def add_urls(bp):
    
    bp.add_url_rule(rule='/', view_func=views.Index.as_view('index'))

