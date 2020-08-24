"""
Service layer for perimetry related operations
"""

from rest_framework.exceptions import ValidationError

from martin_helder.services.body_zone_service import BodyZoneService
from martin_helder.models.perimetry import Perimetry
from martin_helder.models.serializers.perimetry import PerimetrySerializer
from martin_helder.views.view_utils import Utils


class PerimetryService:
    """
    Service class for perimetry related operations
    """

    @staticmethod
    def is_valid_perimetry(perimetry_id):
        """
        Checks if the specified perimetry exists

        :param perimetry_id: if of the perimetry
        """

        Utils.validate_uuid(perimetry_id)

        if not Perimetry.objects.filter(id=perimetry_id).exists():
            raise ValidationError("The perimetry is not valid!")

    @staticmethod
    def add_perimetry(perimetry, id_treatment):
        """
        Creates a perimetry for a new treatment

        :param perimetry: Perimetry info
        :param id_treatment: Corresponding treatment
        :return: Created perimetry
        """

        BodyZoneService.is_valid_body_zone(perimetry['body_zone'])

        new_perimetry = Perimetry.objects.create(size=perimetry['size'],
                                                 body_zone_id=perimetry['body_zone'],
                                                 treatment_id=id_treatment)

        new_perimetry.save()

        return new_perimetry.id

    @staticmethod
    def perimetry_info(perimetry_id):
        """
        Method that acquires information about a specific perimetry

        :param perimetry_id: id of the perimetry
        :return: Serializer of perimetry
        """

        PerimetryService.is_valid_perimetry(perimetry_id)

        try:
            perimetry = Perimetry.objects.get(id=perimetry_id)
        except:
            raise ValidationError("The perimetry is not valid!")

        perimetry_data = PerimetrySerializer(perimetry).data

        return perimetry_data
