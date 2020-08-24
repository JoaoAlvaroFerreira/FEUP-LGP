"""
View layer of all perimetry info related endpoints
"""
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.views.view_utils import Utils
from martin_helder.services.perimetry_service import PerimetryService

from martin_helder.middlewares.jwt_authentication import login_required


class PerimetryInfoView(APIView):
    """
     All endpoints related to perimetry info actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get a perimetry info",
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
                           openapi.Parameter('id_perimetry',
                                             openapi.IN_QUERY,
                                             description="Perimetry id",
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
                'size': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request, id_patient, id_treatment_cycle, id_treatment, id_perimetry):
        """
        Action when calling the endpoint with GET
        """
        PerimetryInfoView.validate_perimetry_info_request(id_patient,
                                                          id_treatment_cycle,
                                                          id_treatment,
                                                          id_perimetry)

        perimetry_info = PerimetryService.perimetry_info(id_perimetry)

        return JsonResponse(perimetry_info)

    @staticmethod
    def validate_perimetry_info_request(id_patient,
                                        id_treatment_cycle,
                                        id_treatment,
                                        id_perimetry):
        """
        Validates the treatment information received in the request body

        :param id_patient: Id of the patient received
        :param id_treatment_cycle: Id of the treatment cycle received
        :param id_treatment: Id of the treatment received
        :param id_perimetry: Id of the perimetry received
        """

        Utils.validate_uuid(id_patient)
        Utils.validate_uuid(id_treatment_cycle)
        Utils.validate_uuid(id_treatment)
        Utils.validate_uuid(id_perimetry)
