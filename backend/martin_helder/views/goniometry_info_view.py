"""
View layer of all goniometry info related endpoints
"""
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.views.view_utils import Utils
from martin_helder.services.goniometry_service import GoniometryService
from martin_helder.middlewares.jwt_authentication import login_required


class GoniometryInfoView(APIView):
    """
     All endpoints related to goniometry info actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get a goniometry info",
        manual_parameters=[openapi.Parameter('id_patient',
                                             openapi.IN_QUERY,
                                             description="Patient id",
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('id_treatment',
                                             openapi.IN_QUERY,
                                             description="Treatment id",
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('id_treatment_cycle',
                                             openapi.IN_QUERY,
                                             description="Treatment cycle id",
                                             type=openapi.TYPE_STRING),
                           openapi.Parameter('id_goniometry',
                                             openapi.IN_QUERY,
                                             description="Goniometry id",
                                             type=openapi.TYPE_STRING),
                           ],
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.FORMAT_UUID),
                'treatment': openapi.Schema(type=openapi.FORMAT_UUID),
                'body_zone': openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                    'id': openapi.Schema(type=openapi.FORMAT_UUID),
                    'name': openapi.Schema(type=openapi.TYPE_STRING)}),
                'min_abduction': openapi.Schema(type=openapi.TYPE_INTEGER),
                'max_abduction': openapi.Schema(type=openapi.TYPE_INTEGER),
                'min_adduction': openapi.Schema(type=openapi.TYPE_INTEGER),
                'max_adduction': openapi.Schema(type=openapi.TYPE_INTEGER),
                'min_flexion': openapi.Schema(type=openapi.TYPE_INTEGER),
                'max_flexion': openapi.Schema(type=openapi.TYPE_INTEGER),
                'min_rotation': openapi.Schema(type=openapi.TYPE_INTEGER),
                'max_rotation': openapi.Schema(type=openapi.TYPE_INTEGER),
                'min_extension': openapi.Schema(type=openapi.TYPE_INTEGER),
                'max_extension': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request, id_patient, id_treatment_cycle, id_treatment, id_goniometry):
        """
        Action when calling the endpoint with GET
        """
        GoniometryInfoView.validate_goniometry_info_request(id_patient,
                                                            id_treatment_cycle,
                                                            id_treatment,
                                                            id_goniometry)

        goniometry_info = GoniometryService.goniometry_info(id_goniometry)

        return JsonResponse(goniometry_info)

    @staticmethod
    def validate_goniometry_info_request(id_patient,
                                         id_treatment_cycle,
                                         id_treatment,
                                         id_goniometry):
        """
        Validates the goniometry information received in the request

        :param id_patient: Id of the patient received
        :param id_treatment_cycle: Id of the treatment cycle received
        :param id_treatment: Id of the treatment received
        :param id_goniometry: Id of the goniometry received
        """

        Utils.validate_uuid(id_patient)
        Utils.validate_uuid(id_treatment_cycle)
        Utils.validate_uuid(id_treatment)
        Utils.validate_uuid(id_goniometry)
