"""
View layer of physiotherapist treatment related endpoints
"""

from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.services.treatment_service import TreatmentService
from martin_helder.views.pagination_view_utils import PaginationViewUtils
from martin_helder.middlewares.jwt_authentication import physio_only, login_required


class TreatmentPhysioView(APIView):
    """
    Endpoint related to physiotherapist list treatment
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get the list of all treatments of a physiotherapist",
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
                        'summary': openapi.Schema(type=openapi.TYPE_STRING),
                        'patient_name': openapi.Schema(type=openapi.TYPE_STRING),
                        'pain_level': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'medication': openapi.Schema(type=openapi.TYPE_STRING),
                        'treatment': openapi.Schema(type=openapi.TYPE_STRING),
                        'periodic_evaluation': openapi.Schema(type=openapi.TYPE_STRING),
                        'treatment_cycle': openapi.Schema(type=openapi.FORMAT_UUID),
                        'url': openapi.Schema(type=openapi.TYPE_STRING),
                        'perimetries': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.FORMAT_UUID),
                                'size': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'treatment': openapi.Schema(type=openapi.FORMAT_UUID),
                                'body_zone': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'id': openapi.Schema(type=openapi.FORMAT_UUID),
                                        'name': openapi.Schema(type=openapi.TYPE_STRING)
                                    }
                                ))
                            }
                        )),
                        'goniometries': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.FORMAT_UUID),
                                'body_zone': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'id': openapi.Schema(type=openapi.FORMAT_UUID),
                                        'name': openapi.Schema(type=openapi.TYPE_STRING)
                                    }
                                )),
                                'treatment': openapi.Schema(type=openapi.FORMAT_UUID),
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
                            }
                        )),
                        'muscle_tests': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.FORMAT_UUID),
                                'body_zone': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
                                    type=openapi.TYPE_OBJECT,
                                    properties={
                                        'id': openapi.Schema(type=openapi.FORMAT_UUID),
                                        'name': openapi.Schema(type=openapi.TYPE_STRING)
                                    }
                                )),
                                'strength': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'treatment': openapi.Schema(type=openapi.FORMAT_UUID)
                            }
                        ))
                    }))
            },
        ), 400: "Error Message"}
    )
    @login_required
    @physio_only
    def get(request):
        """
        Action when calling the endpoint with GET
        Return list of all treatments of physiotherapist

        :param request: request for treatments list
        :return: json response with treatments list
        """

        pagination_args = PaginationViewUtils.get_pagination_args(request)
        current_path = request.build_absolute_uri()

        all_treatment_info = TreatmentService.list_all_physio_treatments(request.auth_user['id'],
                                                                         pagination_args['page_num'],
                                                                         pagination_args['page_size'],
                                                                         current_path)

        return JsonResponse(all_treatment_info, safe=False)
