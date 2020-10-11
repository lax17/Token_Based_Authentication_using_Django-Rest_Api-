from datetime import timedelta
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from .models import AuthTokens
from rest_framework import status
from rest_framework.response import Response
from .responses import APIResponse
from .serializers import APIResponseSerializer


class BaseResponseException(Exception):
    """
    Base Exceptions for response status
    """
    status_code = None
    message = ""
    data = None

    def __init__(self, message, data):
        self.message = message if message else ""
        self.data = data if data else dict()


class RequestBodyException(BaseResponseException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Invalid Request Body"

    def __init__(self, message=None, data=None):
        message = message if message else self.message
        super(self.__class__, self).__init__(message=message, data=data)

class UnauthorizedException(BaseResponseException):
    status_code = status.HTTP_401_UNAUTHORIZED
    message = "Unauthorized Request"


    def __init__(self, message=None, data=None):
        message = message if message else self.message
        super(self.__class__, self).__init__(message=message, data=data)


class InternalServerException(BaseResponseException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Internal Server Error"

    def __init__(self, message=None, data=None):
        message = message if message else self.message
        super(self.__class__, self).__init__(message=message, data=data)


class TokenExpiredException(BaseResponseException):

    status_code = status.HTTP_204_NO_CONTENT
    message = "Token expired."

    def __init__(self, message=None, data=None):
        message = message if message else self.message
        super(self.__class__, self).__init__(message=message, data=data)


def auth_exception_handler(exc, context):
    """
    Handles exceptions derived from BaseResponseException.
    """
    if not isinstance(exc, BaseResponseException):
        return None
    response = APIResponse(status=exc.status_code, message=exc.message, data=exc.data)
    return Response(data=APIResponseSerializer(response).data)




class ClientAuthentication(BaseAuthentication):
    """
    Authentication class to be used for protected APIs used by third parties.
    """

    def authenticate(self, request):
        return self.authenticate_header(request)

    def authenticate_header(self, request):

        header = get_authorization_header(request=request)
        if not header:
            raise UnauthorizedException(message="Missing Authorization header.")
        parts = header.decode().split(" ")
        if len(parts) != 2 or parts[0] != "Basic":
            raise UnauthorizedException(message="Unsupported Authorization header format.")
        try:
            token = AuthTokens.objects.select_related().get(id=parts[1])
            if token.created_at + timedelta(seconds=token.user.expiry_window) <= timezone.now():
                raise TokenExpiredException()
            return token.user, None
        except AuthTokens.DoesNotExist as e:
            raise UnauthorizedException(message="Invalid Token.")

