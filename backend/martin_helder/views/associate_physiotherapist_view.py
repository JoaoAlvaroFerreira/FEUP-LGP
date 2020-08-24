"""
View layer of all associate physiotherapist with patient related endpoints
"""

import json

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.services.patient_physiotherapist_service import PatientPhysioService
from martin_helder.middlewares.jwt_authentication import admin_only, login_required

class AssocPhysioWithPatientView(APIView):
    """
    All endpoints related to associate physiotherapist with patient actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Associate physiotherapist with patient",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['physiotherapist_id'
                      ],
            properties={
                'patient_id': openapi.Schema(type=openapi.FORMAT_UUID),
                'physiotherapist_id': openapi.Schema(type=openapi.FORMAT_UUID),
            },
        ),
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'patient_id': openapi.Schema(type=openapi.FORMAT_UUID),
                'physiotherapist_id': openapi.Schema(type=openapi.FORMAT_UUID),
                'patientphysiotherapist_id': openapi.Schema(type=openapi.FORMAT_UUID),
            },
        ), 400: "Error Message"}
    )
    @login_required
    @admin_only
    def post(request, id_patient):
        """
        Action when calling the endpoint with POST

        :param request: request for associating physiotherapist to patient adding
        :return: json response with new patient info
        """
        assoc_physio_with_patient_request = json.loads(request.body.decode('utf-8'))

        AssocPhysioWithPatientView.validate_assoc_physio_with_patient_request(
            assoc_physio_with_patient_request)

        association_info = PatientPhysioService.assoc_physio_with_patient(
            assoc_physio_with_patient_request, id_patient)

        return JsonResponse(association_info, safe=False)


    @staticmethod
    def validate_assoc_physio_with_patient_request(assoc_physio_with_patient_request):
        """
        Validates the assoc physio with patient information received in the request body

        :param assoc_physio_with_patient_request:
        assoc physio with patient information received in the request
        """

        if 'physiotherapist_id' not in assoc_physio_with_patient_request:
            raise ValidationError("Missing physiotherapist_id in assoc physio with patient request!")
