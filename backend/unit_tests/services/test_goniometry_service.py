"""
Tests related to Goniometry Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase

from martin_helder.services.goniometry_service import GoniometryService
from martin_helder.services.body_zone_service import BodyZoneService
from martin_helder.models import Goniometry

from unit_tests.data_repository import GoniometryDataRepository


class GoniometryServiceTestCase(TestCase):
    """
    Goniometry service test cases
    """

    def setUp(self):
        self.goniometry = GoniometryDataRepository.get_valid_goniometry()
        self.id_treatment = str(uuid.uuid4())

    @patch.object(BodyZoneService, 'is_valid_body_zone')
    @patch.object(Goniometry.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_goniometry(self, mock_goniometry, mock_body_zone_service):
        """
        Tests if the method saves the goniometry successfully

        :param mock_body_zone_service: Mock of the body zone service
        :param mock_goniometry: Mock of the goniometry service
        """

        mock_new_model = mock_goniometry.return_value

        return_value = GoniometryService.add_goniometry(self.goniometry, self.id_treatment)
        mock_body_zone_service.assert_called_once_with(self.goniometry['body_zone'])
        mock_goniometry.assert_called_once_with(body_zone_id=self.goniometry['body_zone'],
                                                min_abduction=self.goniometry['min_abduction'],
                                                max_abduction=self.goniometry['max_abduction'],
                                                min_adduction=self.goniometry['min_adduction'],
                                                max_adduction=self.goniometry['max_adduction'],
                                                min_flexion=self.goniometry['min_flexion'],
                                                max_flexion=self.goniometry['max_flexion'],
                                                min_rotation=self.goniometry['min_rotation'],
                                                max_rotation=self.goniometry['max_rotation'],
                                                min_extension=self.goniometry['min_extension'],
                                                max_extension=self.goniometry['max_extension'],
                                                treatment_id=self.id_treatment)
        mock_new_model.save.assert_called_once_with()

        self.assertEqual(return_value, mock_new_model.id)
