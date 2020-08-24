"""
Tests related to Pagination view utils class
"""

from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.views.pagination_view_utils import PaginationViewUtils
from unit_tests.data_repository import PaginationDataRepository


class PaginationViewUtilsTestCase(TestCase):
    """
    Test case related to Pagination View utils class
    """

    @staticmethod
    def test_true_get_pagination_args():
        """
        Tests if the method returns valid pagination args
        """

        PaginationViewUtils.get_pagination_args(PaginationDataRepository.get_valid_pagination())

    def test_missing_page_num_pagination_args(self):
        """
        Tests if the method detects a pagination request with a missing page number
        """

        self.assertRaises(ValidationError,
                          PaginationViewUtils.get_pagination_args,
                          PaginationDataRepository.get_missing_page_num_pagination())

    def test_missing_page_size_pagination_args(self):
        """
        Tests if the method detects a pagination request with a missing page size
        """

        self.assertRaises(ValidationError,
                          PaginationViewUtils.get_pagination_args,
                          PaginationDataRepository.get_missing_page_size_pagination())

    @staticmethod
    def test_true_validate_pagination_args():
        """
        Tests if the method validates correct pagination args
        """

        PaginationViewUtils.validate_pagination_args(PaginationDataRepository.get_valid_pagination().GET['page_num'],
                                                     PaginationDataRepository.get_valid_pagination().GET['page_size'])

    def test_invalid_page_num_validate_pagination_args(self):
        """
        Tests if the method detects a pagination request with a invalid page number
        """

        self.assertRaises(ValidationError,
                          PaginationViewUtils.validate_pagination_args,
                          PaginationDataRepository.get_invalid_page_num_pagination().GET['page_num'],
                          PaginationDataRepository.get_invalid_page_num_pagination().GET['page_size'])

    def test_non_numeric_page_num_validate_pagination_args(self):
        """
        Tests if the method detects a pagination request with a non numeric page number
        """

        self.assertRaises(ValidationError,
                          PaginationViewUtils.validate_pagination_args,
                          PaginationDataRepository.get_non_numeric_page_num_pagination().GET['page_num'],
                          PaginationDataRepository.get_non_numeric_page_num_pagination().GET['page_size'])

    def test_invalid_page_size_validate_pagination_args(self):
        """
        Tests if the method detects a pagination request with a invalid page size
        """

        self.assertRaises(ValidationError,
                          PaginationViewUtils.validate_pagination_args,
                          PaginationDataRepository.get_invalid_page_size_pagination().GET['page_num'],
                          PaginationDataRepository.get_invalid_page_size_pagination().GET['page_size'])

    def test_non_numeric_page_size_validate_pagination_args(self):
        """
        Tests if the method detects a pagination request with a non numeric page size
        """

        self.assertRaises(ValidationError,
                          PaginationViewUtils.validate_pagination_args,
                          PaginationDataRepository.get_non_numeric_page_size_pagination().GET['page_num'],
                          PaginationDataRepository.get_non_numeric_page_size_pagination().GET['page_size'])
