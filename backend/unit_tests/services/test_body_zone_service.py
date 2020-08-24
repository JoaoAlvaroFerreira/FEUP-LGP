"""
Tests related to Body zone Service class
"""
import uuid
from unittest.mock import patch
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.services.body_zone_service import BodyZoneService


class BodyZoneServiceTestCase(TestCase):
    """
    Body zone service test cases
    """

    def setUp(self):
        self.id_body_zone = str(uuid.uuid4())

    @patch('martin_helder.models.BodyZone.objects')
    def test_valid_is_valid_body_zone(self, mock_body_zone_objects):
        """
        Tests if the method is successful when the body zone from the database is valid

        :param mock_body_zone_objects: Mock of the body zone model
        """

        mock_body_zone_objects.filter.return_value.exists.return_value = True

        BodyZoneService.is_valid_body_zone(self.id_body_zone)
        mock_body_zone_objects.filter.assert_called_once_with(id=self.id_body_zone)
        mock_body_zone_objects.filter.return_value.exists.assert_called_once()

    @patch('martin_helder.models.BodyZone.objects')
    def test_invalid_is_valid_body_zone(self, mock_body_zone_objects):
        """
        Tests if the method raises a validation error when the body zone doesn't exist

        :param mock_body_zone_objects: Mock of the body zone model
        """

        mock_body_zone_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          BodyZoneService.is_valid_body_zone, self.id_body_zone)
        mock_body_zone_objects.filter.assert_called_once_with(id=self.id_body_zone)
        mock_body_zone_objects.filter.return_value.exists.assert_called_once()
