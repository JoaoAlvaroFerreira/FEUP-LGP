"""
Tests related to Muscle Test Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase

from martin_helder.services.body_zone_service import BodyZoneService
from martin_helder.models import MuscleTest
from martin_helder.services.muscle_test_service import MuscleTestService

from unit_tests.data_repository import MuscleTestDataRepository


class MuscleTestServiceTestCase(TestCase):
    """
    Muscle Test service test cases
    """

    def setUp(self):
        self.muscle_test = MuscleTestDataRepository.get_valid_muscle_test()
        self.id_treatment = str(uuid.uuid4())

    @patch.object(BodyZoneService, 'is_valid_body_zone')
    @patch.object(MuscleTest.objects, 'create', return_value=Mock(id=str(uuid.uuid4())))
    def test_add_muscle_test(self, mock_muscle_test, mock_body_zone_service):
        """
        Tests if the method saves the muscle test successfully

        :param mock_body_zone_service: Mock of the body zone service
        :param mock_muscle_test: Mock of the muscle tests service
        """

        mock_new_model = mock_muscle_test.return_value

        return_value = MuscleTestService.add_muscle_test(self.muscle_test, self.id_treatment)
        mock_body_zone_service.assert_called_once_with(self.muscle_test['body_zone'])
        mock_muscle_test.assert_called_once_with(strength=self.muscle_test['strength'],
                                                 body_zone_id=self.muscle_test['body_zone'],
                                                 treatment_id=self.id_treatment)
        mock_new_model.save.assert_called_once_with()

        self.assertEqual(return_value, mock_new_model.id)
