"""
View layer of all body zone related endpoints
"""

from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from martin_helder.services.body_zone_service import BodyZoneService
from martin_helder.views.pagination_view_utils import PaginationViewUtils
from martin_helder.middlewares.jwt_authentication import login_required

class BodyZoneView(APIView):
    """
    All endpoints related to body zone actions
    """

    @staticmethod
    @swagger_auto_schema(
        operation_description="Get a list of body zones",
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
                        'name': openapi.Schema(type=openapi.TYPE_STRING)
                    }))
            },
        ), 400: "Error Message"}
    )
    @login_required
    def get(request):
        """
        Action when calling the endpoint with GET
        Return list of body zones

        :param request: request for body zones list
        :return: json response with body zones list
        """

        pagination_args = PaginationViewUtils.get_pagination_args(request)
        current_path = request.build_absolute_uri()

        query = ""
        if 'query' in request.GET:
            query = request.GET['query']

        body_zones = BodyZoneService.list_body_zones(pagination_args['page_num'], pagination_args['page_size'],
                                                     current_path, query)

        return JsonResponse(body_zones, safe=False)
