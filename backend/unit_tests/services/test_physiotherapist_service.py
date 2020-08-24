"""
Tests related to Physiotherapist Service class
"""
import uuid
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.services.physiotherapist_service import PhysiotherapistService

class PhysiotherapistServiceTestCase(TestCase):
    """
    Body zone service test cases
    """

    def setUp(self):
        self.id_patient = str(uuid.uuid4())
        self.id_physiotherapist = str(uuid.uuid4())

    @patch('martin_helder.models.Physiotherapist.objects')
    @patch('martin_helder.models.PatientPhysiotherapist.objects')
    def test_true_is_physiotherapist_attributed_patient(self, mock_patientphysiotherapist_objects,
                                                        mock_physiotherapist_objects):
        """
        Tests if the method is successful when the physiotherapist is attributed to the given patient

        :param mock_physiotherapist_objects: Mock of the physiotherapist model
        :param mock_patientphysiotherapist_objects: Mock of the patientphysiotherapist model
        """

        physiotherapist_info = Mock(name="physiotherapist_info")
        mock_physiotherapist_objects.get.return_value = physiotherapist_info
        mock_patientphysiotherapist_objects.filter.return_value.exists.return_value = True

        PhysiotherapistService.is_physiotherapist_attributed_patient(self.id_patient, self.id_physiotherapist)
        mock_patientphysiotherapist_objects.filter.assert_called_once_with(patient=self.id_patient,
                                                                           physiotherapist=self.id_physiotherapist)
        mock_patientphysiotherapist_objects.filter.return_value.exists.assert_called_once_with()

    @patch('martin_helder.models.Physiotherapist.objects')
    @patch('martin_helder.models.PatientPhysiotherapist.objects')
    def test_false_is_physiotherapist_attributed_patient(self, mock_patientphysiotherapist_objects,
                                                         mock_physiotherapist_objects):
        """
        Tests if the method raises an error when the physiotherapist is not attributed to the given patient

        :param mock_physiotherapist_objects: Mock of the physiotherapist model
        :param mock_patientphysiotherapist_objects: Mock of the patientphysiotherapist model
        """

        physiotherapist_info = Mock(name="physiotherapist_info")
        mock_physiotherapist_objects.get.return_value = physiotherapist_info
        mock_patientphysiotherapist_objects.filter.return_value.exists.return_value = False

        self.assertRaises(ValidationError,
                          PhysiotherapistService.is_physiotherapist_attributed_patient,
                          self.id_patient,
                          self.id_physiotherapist)
        mock_patientphysiotherapist_objects.filter.assert_called_once_with(patient=self.id_patient,
                                                                           physiotherapist=self.id_physiotherapist)
        mock_patientphysiotherapist_objects.filter.return_value.exists.assert_called_once_with()
