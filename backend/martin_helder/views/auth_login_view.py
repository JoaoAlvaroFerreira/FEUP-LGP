"""
View layer of login endpoint
"""

import json
import re

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from martin_helder.views.credential_view import CredentialView
from martin_helder.services.authentication_service import AuthenticationService


class AuthLoginView(APIView):
    """
    Login endpoint and validator
    """

    @staticmethod
    def validate_login_request(login_request):
        """
        Validates the login information received in the request body

        :param login_request: Login information received in the request
        """

        email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if 'email' not in login_request:
            raise ValidationError("Missing email!")

        if not re.search(email_regex, login_request['email']):
            raise ValidationError("Email is not valid!")

        CredentialView.validate_credential_request(login_request)


    @staticmethod
    @swagger_auto_schema(
        operation_description="Login",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'access': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'token': openapi.Schema(type=openapi.TYPE_STRING),
                        'expiredTime': openapi.Schema(type=openapi.FORMAT_DATETIME)
                    },
                ),
                'refresh': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'token': openapi.Schema(type=openapi.TYPE_STRING),
                        'expiredTime': openapi.Schema(type=openapi.FORMAT_DATETIME)
                    },
                ),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
                'is_admin': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                'id': openapi.Schema(type=openapi.FORMAT_UUID),
            },
        ), 400: "Error Message", 401: "Error Message", 403: "Error Message"}
    )
    def post(request):
        """
        Action when calling the endpoint with POST

        :param request: request for login
        :return: json response with access token, refresh token and user information
        """

        login_request = json.loads(request.body.decode('utf-8'))
        AuthLoginView.validate_login_request(login_request)

        response = AuthenticationService.authenticate(login_request['email'], login_request['password'])

        return JsonResponse(response)
