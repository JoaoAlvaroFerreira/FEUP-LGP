"""
View layer of refresh endpoint
"""

import json
import re

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from martin_helder.services.authentication_service import AuthenticationService


class AuthRecoverView(APIView):
    """
    Reset password endpoint and validator
    """

    @staticmethod
    def validate_recover_request(recover_request):
        """
        Validates the recover password information received in the request body

        :param recover_request: Recover password information received in the request
        """

        if 'email' not in recover_request:
            raise ValidationError("Missing email!")

        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
                    recover_request['email']) is None:
            raise ValidationError('Invalid email format provided!')


    @staticmethod
    @swagger_auto_schema(
        operation_description="Recover password",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
            },
        ),
        responses={200: "A new password was sent to the email provided",
                   400: "Error Message",
                   401: "Error Message",
                   403: "Error Message"}
    )
    def post(request):
        """
        Action when calling the endpoint with POST

        :param request: request for reset password
        :return: Successful or error message
        """

        recover_request = json.loads(request.body.decode('utf-8'))
        AuthRecoverView.validate_recover_request(recover_request)

        AuthenticationService.recover_password(recover_request['email'])

        return HttpResponse("A new password was sent to the email provided")
