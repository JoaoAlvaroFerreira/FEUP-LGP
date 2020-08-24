"""
Tests related to Pagination Service class
"""
from unittest.mock import patch, Mock
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from martin_helder.services.pagination_service import PaginationService
from unit_tests.data_repository import PaginationDataRepository
from unit_tests.data_repository import PaginationLinksDataRepository


class PaginationServiceTestCase(TestCase):
    """
    Pagination service test cases
    """

    def setUp(self):
        self.page_num = int(PaginationDataRepository.get_valid_pagination().GET['page_num'])
        self.page_size = int(PaginationDataRepository.get_valid_pagination().GET['page_size'])
        self.path = PaginationDataRepository.get_valid_pagination().build_absolute_uri()
        self.paginator = Mock(page_range=range(5), num_pages=5, count=25)
        self.host = self.path.split('?')[0]

    def test_valid_is_valid_page_number(self):
        """
        Tests if the method validates a valid page number
        """

        PaginationService.is_valid_page_number(self.paginator, 1)

    def test_invalid_is_valid_page_number(self):
        """
        Tests if the method raises the page number is outside the allowed range
        """

        self.assertRaises(ValidationError,
                          PaginationService.is_valid_page_number, self.paginator, 11)

    @patch.object(PaginationService, 'get_results_page_links')
    def test_get_paginated_results(self, mock_page_links):
        """
        Tests if the method returns the results in paginated form

        :param mock_page_links: Mock of the page links
        """

        mock_page_links_result = mock_page_links.return_value
        results = Mock()
        expected_value = {'page_links': mock_page_links_result, 'total_pages': self.paginator.num_pages,
                          'total_results': self.paginator.count, 'results': results}

        return_value = PaginationService.get_paginated_results(self.paginator, self.page_num, self.path, results)

        mock_page_links.assert_called_once_with(self.path, self.paginator, self.page_num)

        self.assertEqual(return_value, expected_value)

    def test_all_get_results_page_links(self):
        """
        Tests if the method returns the page link on a middle page
        """

        expected_result = PaginationLinksDataRepository.get_all_pagination_links(2, self.page_size,
                                                                                 self.paginator, self.host)

        result = PaginationService.get_results_page_links(self.path, self.paginator, str(2))

        self.assertEqual(result, expected_result)

    def test_first_get_results_page_links(self):
        """
        Tests if the method returns the page link on a first page
        """

        expected_result = PaginationLinksDataRepository.get_first_pagination_links(1, self.page_size,
                                                                                   self.paginator, self.host)

        result = PaginationService.get_results_page_links(self.path, self.paginator, str(1))

        self.assertEqual(result, expected_result)

    def test_last_get_results_page_links(self):
        """
        Tests if the method returns the page link on a last page
        """

        expected_result = PaginationLinksDataRepository.get_last_pagination_links(self.paginator.num_pages,
                                                                                  self.page_size, self.paginator,
                                                                                  self.host)

        result = PaginationService.get_results_page_links(self.path, self.paginator, str(self.paginator.num_pages))

        self.assertEqual(result, expected_result)
