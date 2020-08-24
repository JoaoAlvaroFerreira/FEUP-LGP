"""
Simple endpoint to Hello the World!
"""

from django.http import HttpResponse
from rest_framework.views import APIView
# from martin_helder.middlewares.jwt_authentication import admin_only, physio_only, login_required

class HelloWorld(APIView):
    """
    Simple endpoint class to demo the environment
    """

    @staticmethod
    # @login_required
    # @admin_only
    # @physio_only
    def get(request):
        """
        Action when calling the endpoint with GET
        """

        # print(request.auth_user)
        # {'id': 'cc2905e2-6d94-44fa-9de0-62040200f8f1', 'email': 'test1@email.com', 'is_admin': True}

        request.body.decode('utf-8')  # does nothing
        return HttpResponse("Hello Martin Helder!")
