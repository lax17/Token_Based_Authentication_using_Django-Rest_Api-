from rest_framework.views import exception_handler

from .client_authentication import auth_exception_handler

HANDLERS = (exception_handler, auth_exception_handler,)


def exception_handler(exc, context):
    """
    Handles exceptions using exception handlers defined in HANDLERS
    """

    response = None
    for handler in HANDLERS:
        if response:
            break
        response = handler(exc, context)
    return response
