"""
Service layer for authentication related operations
"""

import jwt

from rest_framework.exceptions import ValidationError, PermissionDenied, NotAuthenticated
from martin_helder.services.credential_service import CredentialService
from martin_helder.services.administrator_service import AdministratorService
from martin_helder.services.physiotherapist_service import PhysiotherapistService
from martin_helder.views.view_utils import Utils
from martin_helder.settings import JWT_SECRET_KEY, ACCESS_TOKEN_EXPIRY_TIME, \
  ACCESS_TOKEN_TYPE, REFRESH_TOKEN_EXPIRY_TIME, REFRESH_TOKEN_TYPE

class AuthenticationService:
    """
    Service class for authentication related operations
    """

    @staticmethod
    def authenticate(email, password):
        '''
        Method that handles basic authentication to user

        :param email: Incoming request
        :param password: Incoming request
        :return: json response with access token, refresh token and user information
        '''

        credential = CredentialService.check_credential(email, password)

        admin = AdministratorService.get_administrator_by_credential(credential['id'])
        physio = PhysiotherapistService.get_physiotherapist_by_credential(credential['id'])

        return AuthenticationService.generate_response(admin, physio)


    @staticmethod
    def refresh(refresh_token):
        '''
        Method that refreshes user session

        :param refresh_token: user refresh token
        :return: json response with access token, refresh token and user information
        '''

        payload = AuthenticationService.process_token(refresh_token, REFRESH_TOKEN_TYPE)

        admin = AdministratorService.get_administrator(payload['id'])
        physio = PhysiotherapistService.get_physiotherapist(payload['id'])

        return AuthenticationService.generate_response(admin, physio)


    @staticmethod
    def generate_response(admin, physio):
        '''
        Method that generates json response for login and token refresh requests

        :param admin: Adminstrator object or None
        :param physio: Physiotherapist object or None
        :return: json response with access token, refresh token and user information
        '''

        if admin:
            user = admin
            is_admin = True
        elif physio:
            user = physio
            is_admin = False
        else:
            raise PermissionDenied("Account not found!")

        if not user['state']['name'] == "active":
            raise PermissionDenied("The account is not active!")

        return {
            "access": {
                "token": AuthenticationService.generate_tokens(user['id'],
                                                               user['person']['email'],
                                                               is_admin,
                                                               ACCESS_TOKEN_TYPE),
                "expiredTime": Utils.get_expire_time(ACCESS_TOKEN_EXPIRY_TIME)
            },
            "refresh": {
                "token": AuthenticationService.generate_tokens(user['id'],
                                                               user['person']['email'],
                                                               is_admin,
                                                               REFRESH_TOKEN_TYPE),
                "expiredTime": Utils.get_expire_time(REFRESH_TOKEN_EXPIRY_TIME)
            },
            "is_admin": is_admin,
            "id": user['id'],
            "first_name": user['person']['first_name'],
            "last_name": user['person']['last_name'],
            "email": user['person']['email']
        }


    @staticmethod
    def generate_tokens(user_id, email, is_admin, token_type):
        '''
        Method that generates access and refresh tokens

        :param user_id: administrator or physiotherapist id
        :param email: user email
        :param is_admin: flag that tells if user is admin or not
        :param token_type: token type
        :return: JWT access or refresh token
        '''

        if token_type == ACCESS_TOKEN_TYPE:
            ttl = ACCESS_TOKEN_EXPIRY_TIME
        elif token_type == REFRESH_TOKEN_TYPE:
            ttl = REFRESH_TOKEN_EXPIRY_TIME

        token_content = {
            "id": user_id,
            "email": email,
            "is_admin": is_admin,
            "token_type": token_type,
            'exp': Utils.get_expire_time(ttl)
        }

        return jwt.encode(token_content, JWT_SECRET_KEY).decode('utf8')


    @staticmethod
    def process_token(token, token_type):
        '''
        Method that validates and decodes access and refresh tokens

        :param token: access or refresh token
        :param token_type: token type
        :return: JWT decoded content
        '''

        try:
            payload = jwt.decode(token, JWT_SECRET_KEY)

            if token_type != payload['token_type']:
                raise NotAuthenticated(f"Invalid token provided: {payload['token_type']} token \
                  should not be used for this request!")

            if payload['is_admin']:
                AdministratorService.is_valid_administrator(payload['id'])
            else:
                PhysiotherapistService.is_valid_physiotherapist(payload['id'])
        except jwt.ExpiredSignature:
            raise NotAuthenticated("Error validating token: session has expired!")
        except (jwt.DecodeError, jwt.InvalidTokenError, ValidationError):
            raise NotAuthenticated("Error validating token!")

        return {
            "id": payload['id'],
            "email": payload['email'],
            "is_admin": payload['is_admin']
        }

    @staticmethod
    def reset_password(user, current_password, new_password):
        '''
        Method that resets password

        :param user: user information
        :param current_password: user current password
        :param new_password: user new password to be changed
        '''

        if user['is_admin']:
            credential_id = AdministratorService.get_administrator(user['id'])['credential']
        else:
            credential_id = PhysiotherapistService.get_physiotherapist(user['id'])['credential']

        CredentialService.reset_password(credential_id, current_password, new_password)

    @staticmethod
    def recover_password(email):
        '''
        Method that recovers password from the provided email account

        :param email: account email
        '''

        CredentialService.recover_password(email)
