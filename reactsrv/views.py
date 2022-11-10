"""
Defines this apps view routes
"""

from flask import render_template


def index():
    """ Serves react html file """
    return render_template('index.html')
