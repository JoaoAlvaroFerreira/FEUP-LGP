"""
View layer of all patient related endpoints
"""

import json

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.services.patient_service import PatientService
from martin_helder.services.physiotherapist_service import PhysiotherapistService
from martin_helder.views.person_view import PersonView
from martin_helder.views.pagination_view_utils import PaginationViewUtils

from martin_helder.middlewares.jwt_authentication import login_required, admin_only


class PatientView(APIView):
    """
    All endpoints related to patient actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Add a patient",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['street',
                      'city',
                      'nif',
                      'first_name',
                      'last_name',
                      'birth_date',
                      'telephone_number',
                      'email',
                      'gender',
                      'profession',
                      'diagnostic',
                      'clinical_history',
                      'zip_code'
                      ],
            properties={
                'address': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'street': openapi.Schema(type=openapi.TYPE_STRING),
                    'city': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
                    'zip_code': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=16),
                }),
                'nif': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=16),
                'zip_code': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'birth_date': openapi.Schema(type=openapi.FORMAT_DATE),
                'telephone_number': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=16),
                'email': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
                'gender': openapi.Schema(type=openapi.TYPE_STRING, enum=['m', 'f']),
                'profession': openapi.Schema(type=openapi.TYPE_STRING, max_lenght=127),
                'diagnostic': openapi.Schema(type=openapi.TYPE_STRING),
                'clinical_history': openapi.Schema(type=openapi.TYPE_STRING)
            },
        ),
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'patient_id': openapi.Schema(type=openapi.FORMAT_UUID),
                'person_id': openapi.Schema(type=openapi.FORMAT_UUID),
            },
        ), 400: "Error Message"}
    )
    @login_required
    @admin_only
    def post(request):
        """
        Action when calling the endpoint with POST

        :param request: request for patient adding
        :return: json response with new patient info
        """
        patient_request = json.loads(request.body.decode('utf-8'))
        PatientView.validate_patient_request(patient_request)

        new_patient_info = PatientService.add_patient(patient_request)

        return JsonResponse(new_patient_info)

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get a list of patients",
        manual_parameters=[openapi.Parameter('page_num', openapi.IN_QUERY, description="Number of specified page",
                                             type=openapi.TYPE_INTEGER),
                           openapi.Parameter('page_size', openapi.IN_QUERY, description="Size of each page",
                                             type=openapi.TYPE_INTEGER),
                           openapi.Parameter('query', openapi.IN_QUERY, description="Search query",
                                             type=openapi.TYPE_STRING),
                           ],
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'page_links': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'first': openapi.Schema(type=openapi.FORMAT_URI),
                    'previous': openapi.Schema(type=openapi.FORMAT_URI),
                    'next': openapi.Schema(type=openapi.FORMAT_URI),
                    'last': openapi.Schema(type=openapi.FORMAT_URI)}),
                'total_pages': openapi.Schema(type=openapi.TYPE_INTEGER),
                'total_results': openapi.Schema(type=openapi.TYPE_INTEGER),
                'results': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.FORMAT_UUID),
                        'name': openapi.Schema(type=openapi.TYPE_STRING),
                        'doctor': openapi.Schema(type=openapi.TYPE_STRING),
                        'state': openapi.Schema(type=openapi.TYPE_STRING)
                    }))
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request):
        """
        Action when calling the endpoint with GET
        Return list of patients

        :param request: request for patients list
        :return: json response with patients list
        """

        pagination_args = PaginationViewUtils.get_pagination_args(request)
        current_path = request.build_absolute_uri()

        query = ""
        if 'query' in request.GET:
            query = request.GET['query']

        if request.auth_user['is_admin']:
            all_patient_info = PatientService.list_patients(pagination_args['page_num'],
                                                            pagination_args['page_size'],
                                                            current_path, query)
        else:
            all_patient_info = PhysiotherapistService.list_physios_patients(request.auth_user['id'],
                                                                            pagination_args['page_num'],
                                                                            pagination_args['page_size'],
                                                                            current_path,
                                                                            query)

        return JsonResponse(all_patient_info, safe=False)

    @staticmethod
    def validate_patient_request(patient_request):
        """
        Validates the patients information received in the request body

        :param patient_request: New patients information received in the request
        """

        if 'profession' not in patient_request:
            raise ValidationError("Missing profession in patient!")

        if 'diagnostic' not in patient_request:
            raise ValidationError("Missing diagnostic in patient!")

        if 'clinical_history' not in patient_request:
            raise ValidationError("Missing clinical history in patient!")

        PersonView.validate_person_request(patient_request)
