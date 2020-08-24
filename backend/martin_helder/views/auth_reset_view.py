"""
View layer of refresh endpoint
"""

import json

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from martin_helder.services.authentication_service import AuthenticationService
from martin_helder.middlewares.jwt_authentication import login_required


class AuthResetView(APIView):
    """
    Reset password endpoint and validator
    """

    @staticmethod
    def validate_reset_request(reset_request):
        """
        Validates the reset password information received in the request body

        :param reset_request: Login information received in the request
        """

        if 'current_password' not in reset_request:
            raise ValidationError("Missing current password!")

        if 'new_password' not in reset_request:
            raise ValidationError("Missing new password!")


    @staticmethod
    @swagger_auto_schema(
        operation_description="Reset password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email'],
            properties={
                'current_password': openapi.Schema(type=openapi.TYPE_STRING),
                'new_password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: "A new password was sent to the email provided",
                   400: "Error Message",
                   401: "Error Message",
                   403: "Error Message"}
    )
    @login_required
    def post(request):
        """
        Action when calling the endpoint with POST

        :param request: request for reset password
        :return: Successful or error message
        """

        reset_request = json.loads(request.body.decode('utf-8'))
        AuthResetView.validate_reset_request(reset_request)

        print(request.auth_user)
        AuthenticationService.reset_password(request.auth_user,
                                             reset_request['current_password'],
                                             reset_request['new_password'])

        return HttpResponse("Password was updated successfully")
