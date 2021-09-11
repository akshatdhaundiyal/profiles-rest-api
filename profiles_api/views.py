from rest_framework.views import APIView
# When API calls, it uses this Response module
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Test API View"""

    def get(self, request,format=None):
        """ Returns a list of APIView features"""
        # To demostrate the return of some list/object in APIView
        an_apiview = [
        'Uses HTTPP methods as function (get,post,patch,put,delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your application logic',
        'Is mapped manually to URLs'
        ]
        # ^ Expecting a Response object
