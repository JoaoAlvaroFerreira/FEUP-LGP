"""
Tests related to ViewUtils class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.view_utils import Utils
from data_repository import UtilsDataRepository


class ViewUtilsTestCase(TestCase):
    """
    Test case related to Utils class
    """

    def test_valid_uuid_is_valid(self):
        """
        Tests if the method validate_uuid validates a correct uuid
        """

        try:
            Utils.validate_uuid(UtilsDataRepository.get_valid_uuid())
        except ValidationError:
            self.fail('There should be no validation error.')

    def test_invalid_uuid_is_valid(self):
        """
        Tests if the method validate_uuid raises exception for an incorrect uuid
        """

        self.assertRaises(ValidationError,
                          Utils.validate_uuid,
                          UtilsDataRepository.get_invalid_uuid())
