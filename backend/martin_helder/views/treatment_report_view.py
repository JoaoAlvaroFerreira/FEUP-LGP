"""
View layer of all treatment report related endpoints
"""

from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import FileResponse

from martin_helder.views.view_utils import Utils
from martin_helder.views.treatment_info_view import TreatmentInfoView
from martin_helder.services.treatment_service import TreatmentService

from martin_helder.middlewares.jwt_authentication import login_required


class TreatmentReportView(APIView):
    """
     All endpoints related to treatment report actions
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
            type=openapi.TYPE_FILE,
            description="A PDF treatment report file"
        ), 400: "Error Message"},
        content="application/pdf"
    )
    @login_required
    def get(request, id_patient, id_treatment_cycle, id_treatment):
        """
        Action when calling the endpoint with GET
        """
        TreatmentInfoView.validate_treatment_info_request(id_patient,
                                                          id_treatment_cycle,
                                                          id_treatment)

        treatment_report = TreatmentService.treatment_report(id_treatment)

        return FileResponse(treatment_report, filename=id_treatment+'_report.pdf')

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
