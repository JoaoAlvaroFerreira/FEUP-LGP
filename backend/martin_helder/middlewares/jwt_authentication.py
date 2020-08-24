"""
Custom Middleware and Decorators
"""

import contextlib
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import HttpResponse
from martin_helder.services.authentication_service import AuthenticationService

PREFIX = 'Bearer '


def admin_only(function):
    '''
    Decorator to check if authenticated user is admin
    '''

    def wrapper(request, *args, **kwargs):
        if hasattr(request, 'auth_user') and request.auth_user['is_admin']:
            return function(request, *args, **kwargs)

        return HttpResponse('Administrator permission needed to perform this request', status=401)

    return wrapper

def physio_only(function):
    '''
    Decorator to check if authenticated user is a physiotherapist
    '''

    def wrapper(request, *args, **kwargs):
        if hasattr(request, 'auth_user') and not request.auth_user['is_admin']:
            return function(request, *args, **kwargs)

        return HttpResponse('Physiotherapist permission needed to perform this request', status=401)

    return wrapper

def login_required(function):
    '''
    Decorator to check if user is authenticated
    '''

    def wrapper(request, *args, **kwargs):
        if hasattr(request, 'auth_user') and request.auth_user is not None:
            return function(request, *args, **kwargs)

        return HttpResponse('Missing or invalid format for mandatory Authorization header', status=401)

    return wrapper


class JWTAuthenticationMiddleware(MiddlewareMixin):
    """
    Middleware class to handle jwt access token
    """

    def process_request(self, request):
        """
        Method that processes the request and adds the authenticated user to it

        :param request: Request information
        """
        request.auth_user = self.__class__.get_jwt_user(request)

    @staticmethod
    def get_jwt_user(request):
        """
        Method that decodes token and gets authenticated user

        :param request: Request information
        :return: Authenticated user
        """

        token = request.META.get('HTTP_AUTHORIZATION', None)

        user = None
        if token is not None:
            with contextlib.suppress(Exception):
                user = AuthenticationService.process_token(JWTAuthenticationMiddleware.get_token(token),
                                                           settings.ACCESS_TOKEN_TYPE)

        return user

    @staticmethod
    def get_token(header):
        """
        Method that extracts token from a Bearer token

        :param header: Request token header
        :return: Access token
        """

        if not header.startswith(PREFIX):
            return HttpResponse('Invalid Bearer token provided!', status=401)

        return header[len(PREFIX):]
