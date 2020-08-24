"""
View layer of all doctor related endpoints
"""
import json
import re

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.services.doctor_service import DoctorService
from martin_helder.middlewares.jwt_authentication import admin_only, login_required


class DoctorView(APIView):
    """
     All endpoints related to doctors actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Add a new doctor",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['name,professional_certificate,email,state_id'],
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'professional_certificate': openapi.Schema(type=openapi.TYPE_STRING, maxlenght=16),
                'email': openapi.Schema(type=openapi.FORMAT_EMAIL),
                'medication': openapi.Schema(type=openapi.TYPE_STRING),
                'state_id': openapi.Schema(type=openapi.FORMAT_UUID)
            },
        ),
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'doctor_id': openapi.Schema(type=openapi.FORMAT_UUID)
            },
        ), 400: "Error Message"}
    )
    @login_required
    @admin_only
    def post(request):
        """
        Action when calling the endpoint with POST
        """
        new_doctor_request = json.loads(request.body.decode('utf-8'))
        DoctorView.validate_new_doctor_request(new_doctor_request)

        new_doctor_id = DoctorService.add_doctor(new_doctor_request)

        return JsonResponse(new_doctor_id)

    @staticmethod
    def validate_new_doctor_request(new_doctor_request):
        """
        Validates the new doctor information received in the request body

        :param new_doctor_request: Doctor information received in the request
        """

        if 'name' not in new_doctor_request:
            raise ValidationError("Missing doctor name!")

        if 'professional_certificate' not in new_doctor_request:
            raise ValidationError("Doctor must have a professional certificate!")

        if len(new_doctor_request['professional_certificate']) > 16:
            raise ValidationError("Doctor professional certificate is too long!")

        email_regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if 'email' not in new_doctor_request:
            raise ValidationError("Doctor must have an email!")

        if not re.search(email_regex, new_doctor_request['email']):
            raise ValidationError("Doctor email is not valid!")

        if 'state_id' not in new_doctor_request:
            raise ValidationError("Doctor must have an state!")
