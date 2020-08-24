"""
Tests related to Query Service class
"""

from unittest.mock import patch, Mock
from django.test import TestCase
from django.contrib.postgres.search import SearchQuery, SearchVector

from martin_helder.services.query_service import QueryService
from unit_tests.data_repository import SearchStructureDataRepository


class QueryServiceTestCase(TestCase):
    """
    Query service test cases
    """

    def setUp(self):
        self.query = "test"
        self.search_structure = SearchStructureDataRepository.get_valid_search_structure()

    @patch.object(QueryService, 'build_search_vector')
    @patch.object(SearchQuery, '__init__', return_value=None)
    def test_get_query_results(self, mock_search_query, mock_build_search_vector):
        """
        Tests if the method returns the query search results

        :param mock_build_search_vector: Mock of the search vector builder
        :param mock_search_query: Mock of the search query library
        """

        model = Mock()
        model.objects = Mock()
        model.objects.annotate.return_value.filter.return_value.order_by.return_value = Mock()

        expected_result = model.objects.annotate.return_value.filter.return_value.order_by.return_value

        result = QueryService.get_query_results(model.objects, self.query, self.search_structure)

        mock_build_search_vector.assert_called_once_with(self.search_structure)
        mock_search_query.assert_called_once_with(self.query)

        self.assertEqual(result, expected_result)

    @patch.object(QueryService, 'build_search_vector')
    @patch.object(SearchQuery, '__init__', return_value=None)
    def test_all_get_query_results(self, mock_search_query, mock_build_search_vector):
        """
        Tests if the method returns all models when the query is empty

        :param mock_build_search_vector: Mock of the search vector builder
        :param mock_search_query: Mock of the search query library
        """

        model = Mock()
        model.objects = Mock()
        model.objects.all.return_value = Mock()

        expected_result = model.objects.all.return_value

        result = QueryService.get_query_results(model.objects, "", self.search_structure)

        mock_build_search_vector.assert_not_called()
        mock_search_query.assert_not_called()

        self.assertEqual(result, expected_result)

    def test_build_search_vector(self):
        """
        Tests if the method returns a built search vector
        """

        expected_result = SearchVector('firstColumn', weight='A') + SearchVector('secondColumn', weight='B') \
        + SearchVector('thirdColumn', weight='C') + SearchVector('fourthColumn', weight='D')

        result = QueryService.build_search_vector(SearchStructureDataRepository.get_valid_search_structure())

        self.assertEqual(result, expected_result)
