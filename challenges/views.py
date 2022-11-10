"""
Defines this apps view routes
"""

from flask.views import View


class Challenge(View):
    """ Challenge data view """
    methods = ['GET',]

    def dispatch_request(self):
        """ Returns challenge data """
        return {'error': 'not yet implemented'}
