"""
Service layer for pagination related operations
"""
import re

from rest_framework.exceptions import ValidationError


class PaginationService:
    """
    Service class for pagination related operations
    """

    @staticmethod
    def is_valid_page_number(paginator, page_num):
        """
        Checks if the specified page number is between bounds

        :param paginator: Paginator class
        :param page_num: Specified page number
        """

        if page_num not in paginator.page_range:
            raise ValidationError("Invalid Page Number!")

    @staticmethod
    def get_paginated_results(paginator, page_num, path, results):
        """
        Formats the given results in the complete paginated output

        :param paginator: Paginator class
        :param page_num: Specified page number
        :param path: Current endpoint url
        :param results: Results to be presented
        :return: Formatted results
        """

        result = {'page_links': PaginationService.get_results_page_links(path, paginator, page_num),
                  'total_pages': paginator.num_pages, 'total_results': paginator.count, 'results': results}

        return result

    @staticmethod
    def get_results_page_links(path, paginator, page_num):
        """
        Generates the other pages links section

        :param path: Current endpoint url
        :param paginator: Paginator class
        :param page_num: Specified page number
        :return: Generated other page links
        """
        ret = {'first': re.sub(r'page_num=\d{' + str(len(page_num)) + '}',
                               'page_num=1', path)}

        if int(page_num) > 1:
            ret['previous'] = re.sub(r'page_num=\d{' + str(len(page_num)) + '}',
                                     'page_num=' + str(int(page_num) - 1), path)

        if int(page_num) < paginator.num_pages:
            ret['next'] = re.sub(r'page_num=\d{' + str(len(page_num)) + '}',
                                 'page_num=' + str(int(page_num) + 1), path)

        ret['last'] = re.sub(r'page_num=\d{' + str(len(page_num)) + '}',
                             'page_num=' + str(paginator.num_pages), path)

        return ret
