"""
View layer of all treatment related endpoints
"""
import json

from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.services.treatment_service import TreatmentService
from martin_helder.views.perimetry_view import PerimetryView
from martin_helder.views.muscle_test_view import MuscleTestView
from martin_helder.views.goniometry_view import GoniometryView

from martin_helder.views.pagination_view_utils import PaginationViewUtils

from martin_helder.middlewares.jwt_authentication import login_required, physio_only

class TreatmentView(APIView):
    """
     All endpoints related to treatment actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Treat a patient",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['start_date'],
            properties={
                'start_date': openapi.Schema(type=openapi.FORMAT_DATETIME),
                'end_date': openapi.Schema(type=openapi.FORMAT_DATETIME),
                'pain_level': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=10),
                'medication': openapi.Schema(type=openapi.TYPE_STRING),
                'summary': openapi.Schema(type=openapi.TYPE_STRING),
                'treatment': openapi.Schema(type=openapi.TYPE_STRING),
                'periodic_evaluation': openapi.Schema(type=openapi.TYPE_STRING),
                'perimetries': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    required=['size', 'body_zone'],
                    properties={
                        'size': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=100),
                        'body_zone': openapi.Schema(type=openapi.FORMAT_UUID),
                    },
                )),
                'muscle_tests': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    required=['strength', 'body_zone'],
                    properties={
                        'strength': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=5),
                        'body_zone': openapi.Schema(type=openapi.FORMAT_UUID),
                    },
                )),
                'goniometries': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    required=['strength', 'body_zone'],
                    properties={
                        'min_abduction': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'max_abduction': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'min_adduction': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'max_adduction': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'min_flexion': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'max_flexion': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'min_rotation': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'max_rotation': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'min_extension': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'max_extension': openapi.Schema(type=openapi.TYPE_INTEGER, min=0, max=180),
                        'body_zone': openapi.Schema(type=openapi.FORMAT_UUID),
                    },
                )),
            },
        ),
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'treatment_id': openapi.Schema(type=openapi.FORMAT_UUID),
                'perimetries': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.FORMAT_UUID)),
                'muscle_tests': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.FORMAT_UUID)),
                'goniometries': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.FORMAT_UUID)),
            },
        ), 400: "Error Message"}
    )
    @login_required
    @physio_only
    def post(request, id_patient, id_treatment_cycle):
        """
        Action when calling the endpoint with POST
        """
        treatment_request = json.loads(request.body.decode('utf-8'))
        TreatmentView.validate_treatment_request(treatment_request)

        new_treatment_info = TreatmentService.treat_patient(treatment_request,
                                                            id_patient,
                                                            id_treatment_cycle,
                                                            request.auth_user['id'])

        return JsonResponse(new_treatment_info)

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get the list of all treatments in treatment cycle",
        manual_parameters=[openapi.Parameter('page_num', openapi.IN_QUERY, description="Number of specified page",
                                             type=openapi.TYPE_INTEGER),
                           openapi.Parameter('page_size', openapi.IN_QUERY, description="Size of each page",
                                             type=openapi.TYPE_INTEGER),
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
                        'start_date': openapi.Schema(type=openapi.FORMAT_DATE),
                        'end_date': openapi.Schema(type=openapi.FORMAT_DATE),
                        'summary': openapi.Schema(type=openapi.TYPE_STRING)
                    }))
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request, id_patient, id_treatment_cycle):
        """
        Action when calling the endpoint with GET
        Return list of treatments of treatment cycle

        :param id_treatment_cycle:
        :param id_patient:
        :param request: request for treatments list
        :return: json response with treatments list
        """

        pagination_args = PaginationViewUtils.get_pagination_args(request)
        current_path = request.build_absolute_uri()

        all_treatment_info = TreatmentService.list_all_treatments(id_patient, id_treatment_cycle,
                                                                  pagination_args['page_num'],
                                                                  pagination_args['page_size'],
                                                                  current_path)

        return JsonResponse(all_treatment_info, safe=False)

    @staticmethod
    def validate_treatment_request(treatment_request):
        """
        Validates the treatment information received in the request body

        :param treatment_request: Treatment information received in the request
        """

        if 'start_date' not in treatment_request:
            raise ValidationError("Missing start date!")

        if ('end_date' in treatment_request and
                treatment_request['start_date'] >= treatment_request['end_date']):
            raise ValidationError("End date must be after start date!")

        if ('pain_level' in treatment_request and
                (not isinstance(treatment_request['pain_level'], int) or not
                 0 <= treatment_request['pain_level'] <= 10)):
            raise ValidationError("Pain level must be a number between 0 and 10!")

        if ('summary' in treatment_request and
                not isinstance(treatment_request['summary'], str)):
            raise ValidationError("Summary must be a string!")

        if ('perimetries' in treatment_request and
                not isinstance(treatment_request['perimetries'], list)):
            raise ValidationError("Perimetries must be a list!")

        if 'perimetries' in treatment_request:
            for perimetry in treatment_request['perimetries']:
                PerimetryView.validate_perimetry_request(perimetry)

        if 'muscle_tests' in treatment_request:
            for muscle_test in treatment_request['muscle_tests']:
                MuscleTestView.validate_muscle_test_request(muscle_test)

        if 'goniometries' in treatment_request:
            for goniometry in treatment_request['goniometries']:
                GoniometryView.validate_goniometry_request(goniometry)
