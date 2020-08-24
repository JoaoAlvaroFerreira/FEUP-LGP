"""
Tests related to Perimetry Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase

from martin_helder.services.body_zone_service import BodyZoneService
from martin_helder.models import Perimetry
from martin_helder.services.perimetry_service import PerimetryService

from unit_tests.data_repository import PerimetryDataRepository


class PerimetryServiceTestCase(TestCase):
    """
    Perimetry service test cases
    """

    def setUp(self):
        self.perimetry = PerimetryDataRepository.get_valid_perimetry()
        self.id_treatment = str(uuid.uuid4())

    @patch.object(BodyZoneService, 'is_valid_body_zone')
    @patch.object(Perimetry.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_muscle_test(self, mock_perimetry, mock_body_zone_service):
        """
        Tests if the method saves the perimetry successfully

        :param mock_body_zone_service: Mock of the body zone service
        :param mock_perimetry: Mock of the perimetry model
        """

        mock_new_model = mock_perimetry.return_value

        return_value = PerimetryService.add_perimetry(self.perimetry, self.id_treatment)
        mock_body_zone_service.assert_called_once_with(self.perimetry['body_zone'])
        mock_perimetry.assert_called_once_with(size=self.perimetry['size'],
                                               body_zone_id=self.perimetry['body_zone'],
                                               treatment_id=self.id_treatment)
        mock_new_model.save.assert_called_once_with()

        self.assertEqual(return_value, mock_new_model.id)
