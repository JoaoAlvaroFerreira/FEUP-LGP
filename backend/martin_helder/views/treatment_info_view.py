"""
View layer of all treatment info related endpoints
"""
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.views.view_utils import Utils
from martin_helder.services.treatment_service import TreatmentService

from martin_helder.middlewares.jwt_authentication import login_required


class TreatmentInfoView(APIView):
    """
     All endpoints related to treatment info actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get a treatment info",
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
                           ],
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.FORMAT_UUID),
                'start_date': openapi.Schema(type=openapi.TYPE_STRING),
                'end_date': openapi.Schema(type=openapi.TYPE_STRING),
                'summary': openapi.Schema(type=openapi.TYPE_STRING),
                'pain_level': openapi.Schema(type=openapi.TYPE_INTEGER),
                'medication': openapi.Schema(type=openapi.TYPE_STRING),
                'treatment': openapi.Schema(type=openapi.TYPE_STRING),
                'periodic_evaluation': openapi.Schema(type=openapi.TYPE_STRING),
                'treatment_cycle': openapi.Schema(type=openapi.FORMAT_UUID)
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request, id_patient, id_treatment_cycle, id_treatment):
        """
        Action when calling the endpoint with GET
        """
        TreatmentInfoView.validate_treatment_info_request(id_patient,
                                                          id_treatment_cycle,
                                                          id_treatment)

        treatment_info = TreatmentService.treatment_info(id_treatment)

        return JsonResponse(treatment_info)

    @staticmethod
    def validate_treatment_info_request(id_patient,
                                        id_treatment_cycle,
                                        id_treatment):
        """
        Validates the treatment information received in the request body

        :param id_patient: Id of the patient received
        :param id_treatment_cycle: Id of the treatment cycle received
        :param id_treatment: Id of the treatment received
        """

        Utils.validate_uuid(id_patient)
        Utils.validate_uuid(id_treatment_cycle)
        Utils.validate_uuid(id_treatment)
