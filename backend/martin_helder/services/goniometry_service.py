"""
Service layer for goniometry related operations
"""

from rest_framework.exceptions import ValidationError

from martin_helder.services.body_zone_service import BodyZoneService
from martin_helder.models.goniometry import Goniometry
from martin_helder.models.serializers.goniometry import GoniometrySerializer
from martin_helder.views.view_utils import Utils


class GoniometryService:
    """
    Service class for goniometry related operations
    """

    @staticmethod
    def is_valid_goniometry(goniometry_id):
        """
        Checks if the specified goniometry exists

        :param goniometry_id: if of the goniometry
        """

        Utils.validate_uuid(goniometry_id)

        if not Goniometry.objects.filter(id=goniometry_id).exists():
            raise ValidationError("The goniometry is not valid!")

    @staticmethod
    def add_goniometry(goniometry, id_treatment):
        """
        Creates a goniometry for a new treatment

        :param goniometry: Goniometry info
        :param id_treatment: Corresponding treatment
        :return: Created goniometry
        """

        BodyZoneService.is_valid_body_zone(goniometry['body_zone'])

        new_goniometry = Goniometry.objects.create(body_zone_id=goniometry['body_zone'],
                                                   min_abduction=goniometry['min_abduction'],
                                                   max_abduction=goniometry['max_abduction'],
                                                   min_adduction=goniometry['min_adduction'],
                                                   max_adduction=goniometry['max_adduction'],
                                                   min_flexion=goniometry['min_flexion'],
                                                   max_flexion=goniometry['max_flexion'],
                                                   min_rotation=goniometry['min_rotation'],
                                                   max_rotation=goniometry['max_rotation'],
                                                   min_extension=goniometry['min_extension'],
                                                   max_extension=goniometry['max_extension'],
                                                   treatment_id=id_treatment)

        new_goniometry.save()

        return new_goniometry.id


    @staticmethod
    def goniometry_info(goniometry_id):
        """
        Method that acquires information about a specific goniometry

        :param goniometry_id: id of the goniometry
        :return: Serializer of goniometry
        """

        GoniometryService.is_valid_goniometry(goniometry_id)

        try:
            goniometry = Goniometry.objects.get(id=goniometry_id)
        except:
            raise ValidationError("The goniometry is not valid!")

        goniometry_data = GoniometrySerializer(goniometry).data

        return goniometry_data
