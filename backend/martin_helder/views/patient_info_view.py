"""
View layer of all patient related endpoints
"""

from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.services.patient_service import PatientService
from martin_helder.middlewares.jwt_authentication import login_required



class PatientInfoView(APIView):
    """
    All endpoints related to patient info actions
    """
    @staticmethod
    @swagger_auto_schema(
        operation_description="Get a patient info",
        manual_parameters=[openapi.Parameter('id_patient', openapi.IN_QUERY, description="Patient id",
                                             type=openapi.TYPE_STRING),
                           ],
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.FORMAT_UUID),
                'person': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': openapi.Schema(type=openapi.FORMAT_UUID),
                    'address': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'id': openapi.Schema(type=openapi.FORMAT_UUID),
                        'street': openapi.Schema(type=openapi.TYPE_STRING),
                        'zip_code': openapi.Schema(type=openapi.TYPE_STRING),
                        'city': openapi.Schema(type=openapi.TYPE_STRING)}),
                    'nif': openapi.Schema(type=openapi.TYPE_INTEGER),
                    'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                    'birth_date    ': openapi.Schema(type=openapi.TYPE_STRING),
                    'telephone_number': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'gender': openapi.Schema(type=openapi.TYPE_STRING)}),
                'doctor': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': openapi.Schema(type=openapi.FORMAT_UUID),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'professional_certificate': openapi.Schema(type=openapi.TYPE_STRING),
                    'email': openapi.Schema(type=openapi.TYPE_STRING),
                    'state': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                        'id': openapi.Schema(type=openapi.FORMAT_UUID),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'description': openapi.Schema(type=openapi.TYPE_STRING)
                        })}),
                'state': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': openapi.Schema(type=openapi.FORMAT_UUID),
                    'name': openapi.Schema(type=openapi.TYPE_STRING),
                    'description': openapi.Schema(type=openapi.TYPE_STRING)}),
                'profession': openapi.Schema(type=openapi.FORMAT_UUID),
                'diagnostic': openapi.Schema(type=openapi.TYPE_STRING),
                'clinical_history': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request, id_patient):
        """
        Action when calling the endpoint with GET

        :param request: GET request for patient information
        :return: json response with patient info
        """

        return JsonResponse(PatientService.patient_info(id_patient))
