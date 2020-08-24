"""
Useful methods for pagination management on View layer
"""
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView


class PaginationViewUtils(APIView):
    """
    Useful methods for pagination management on View layer
    """

    @staticmethod
    def get_pagination_args(request):
        """
        Obtains and checks the pagination GET parameters

        :param request: GET Request
        :return: Pagination parameters dictionary
        """

        if 'page_num' not in request.GET:
            raise ValidationError("Current page number not specified!")

        page_num = request.GET['page_num']

        if 'page_size' not in request.GET:
            raise ValidationError("Page size not specified!")

        page_size = request.GET['page_size']

        PaginationViewUtils.validate_pagination_args(page_num, page_size)

        return {"page_num": page_num, "page_size": page_size}

    @staticmethod
    def validate_pagination_args(page_num, page_size):
        """
        Validation of Pagination arguments

        :param page_num: Specified page number
        :param page_size: Number of elements per page
        """

        if not page_num.isnumeric():
            raise ValidationError("Current page number must be a number!")

        if int(page_num) <= 0:
            raise ValidationError("Page number must be greater than 1!")

        if not page_size.isnumeric():
            raise ValidationError("Page size must be a number!")

        if int(page_size) <= 0:
            raise ValidationError("Page size must be greater than 1!")
