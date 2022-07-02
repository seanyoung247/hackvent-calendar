"""
Defines this apps view routes
"""

from flask.views import View


class Challenge(View):
    methods = ['GET',]
    
    def dispatch_request(self):
        return {'error': 'not yet implemented'}

