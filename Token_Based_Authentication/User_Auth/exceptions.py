from rest_framework import status

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


class TokenExpiredException(BaseResponseException):

    status_code = status.HTTP_204_NO_CONTENT
    message = "Token expired."

    def __init__(self, message=None, data=None):
        message = message if message else self.message
        super(self.__class__, self).__init__(message=message, data=data)