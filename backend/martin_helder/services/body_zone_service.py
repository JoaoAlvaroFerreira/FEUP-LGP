"""
Service layer for body zone related operations
"""

from django.core.paginator import Paginator
from rest_framework.exceptions import ValidationError
from martin_helder.models import BodyZone

from martin_helder.services.query_service import QueryService
from martin_helder.services.pagination_service import PaginationService
from martin_helder.views.view_utils import Utils
from martin_helder.models.bodyzone import BodyZoneSerializer

class BodyZoneService:
    """
    Service class for body zone related operations
    """

    @staticmethod
    def is_valid_body_zone(id_body_zone):
        """
        Checks if the specified body zone exists

        :param id_body_zone: ID of body zone to be checked
        """

        Utils.validate_uuid(id_body_zone)

        if not BodyZone.objects.filter(id=id_body_zone).exists():
            raise ValidationError("The body zone " + id_body_zone + " is not valid!")

    @staticmethod
    def list_body_zones(page_num, page_size, path, query=""):
        """
        Method to list body zones on the system

        :param page_num: Specified page number
        :param page_size: Specified number of elements per page
        :param path: Current endpoint url
        :param query: Search query
        :return: list of body zones on the system
        """

        body_zones_list = QueryService.get_trigram_similarity_results(BodyZone, query)

        paginator = Paginator(body_zones_list, page_size)

        PaginationService.is_valid_page_number(paginator, int(page_num))
        results = BodyZoneSerializer(paginator.page(page_num), many=True).data

        return PaginationService.get_paginated_results(paginator, page_num, path, results)
