"""
View layer of all patient related endpoints
"""

import json

from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from martin_helder.services.administrator_service import AdministratorService
from martin_helder.views.person_view import PersonView
from martin_helder.middlewares.jwt_authentication import admin_only, login_required


class AdministratorView(APIView):
    """
    All endpoints related to administrator actions
    """

    @staticmethod
    def validate_add_administrator_request(administrator_request):
        """
        Validates the administrator information received in the request body

        :param administrator_request: New administrators information received in the request
        """

        PersonView.validate_person_request(administrator_request)

    @staticmethod
    @swagger_auto_schema(
        operation_description="Add an administrator",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['street', 'city', 'nif', 'first_name', 'last_name', 'birth_date',
                      'telephone_number', 'email', 'gender', 'password', 'zip_code'],
            properties={
                'address': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'street': openapi.Schema(type=openapi.TYPE_STRING),
                    'city': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
                    'zip_code': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=16),
                }),
                'nif': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=16),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'birth_date': openapi.Schema(type=openapi.FORMAT_DATE),
                'telephone_number': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=16),
                'email': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
                'gender': openapi.Schema(type=openapi.TYPE_STRING, enum=['m', 'f']),
                'state': openapi.Schema(type=openapi.FORMAT_UUID),
            },
        ),
        responses={201: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'administrator_id': openapi.Schema(type=openapi.FORMAT_UUID),
                'person_id': openapi.Schema(type=openapi.FORMAT_UUID),
            },
        ), 400: "Error Message"}
    )
    @login_required
    @admin_only
    def post(request):
        """
        Action when calling the endpoint with POST

        :param request: request for administrator adding
        :return: json response with new administrator info
        """
        administrator_request = json.loads(request.body.decode('utf-8'))
        AdministratorView.validate_add_administrator_request(administrator_request)

        new_administrator_info = AdministratorService.add_administrator(administrator_request)

        return JsonResponse(new_administrator_info, status=201)
