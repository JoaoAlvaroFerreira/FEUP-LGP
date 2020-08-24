"""
Init Middleware layer
"""

from .jwt_authentication import JWTAuthenticationMiddleware

__all__ = ["JWTAuthenticationMiddleware"]
