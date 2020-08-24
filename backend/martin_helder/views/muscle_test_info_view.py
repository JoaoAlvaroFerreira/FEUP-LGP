"""
View layer of all muscle test info related endpoints
"""
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.views.view_utils import Utils
from martin_helder.services.muscle_test_service import MuscleTestService

from martin_helder.middlewares.jwt_authentication import login_required


class MuscleTestInfoView(APIView):
    """
     All endpoints related to muscle test info actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get a muscle test info",
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
                           openapi.Parameter('id_muscle_test',
                                             openapi.IN_QUERY,
                                             description="Muscle Test id",
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
                'strength': openapi.Schema(type=openapi.TYPE_INTEGER)
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request, id_patient, id_treatment_cycle, id_treatment, id_muscle_test):
        """
        Action when calling the endpoint with GET
        """
        MuscleTestInfoView.validate_muscle_test_info_request(id_patient,
                                                             id_treatment_cycle,
                                                             id_treatment,
                                                             id_muscle_test)

        muscle_test_info = MuscleTestService.muscle_test_info(id_muscle_test)

        return JsonResponse(muscle_test_info)

    @staticmethod
    def validate_muscle_test_info_request(id_patient,
                                          id_treatment_cycle,
                                          id_treatment,
                                          id_muscle_test):
        """
        Validates the treatment information received in the request body

        :param id_patient: Id of the patient received
        :param id_treatment_cycle: Id of the treatment cycle received
        :param id_treatment: Id of the treatment received
        :param id_muscle_test: Id of the muscle test received
        """

        Utils.validate_uuid(id_patient)
        Utils.validate_uuid(id_treatment_cycle)
        Utils.validate_uuid(id_treatment)
        Utils.validate_uuid(id_muscle_test)
