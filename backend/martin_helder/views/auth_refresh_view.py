"""
View layer of refresh endpoint
"""

import json

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from martin_helder.services.authentication_service import AuthenticationService


class AuthRefreshView(APIView):
    """
    Refresh token endpoint and validator
    """

    @staticmethod
    def validate_refresh_request(refresh_request):
        """
        Validates the refresh information received in the request body

        :param refresh_request: Login information received in the request
        """

        if 'refresh_token' not in refresh_request:
            raise ValidationError("Missing refresh token!")


    @staticmethod
    @swagger_auto_schema(
        operation_description="Refresh token",
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

        :param request: request for refresh token
        :return: json response with access token, refresh token and user information
        """

        refresh_request = json.loads(request.body.decode('utf-8'))
        AuthRefreshView.validate_refresh_request(refresh_request)

        response = AuthenticationService.refresh(refresh_request['refresh_token'])

        return JsonResponse(response)
