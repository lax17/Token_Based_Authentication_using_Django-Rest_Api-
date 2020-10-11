

class APIResponse(object):
    """
    Used for API response creation
    """

    def __init__(self, status, message="", data=None):
        self.status = status
        self.message = message
        self.data = data if data else dict()

class FunctionResponse(object):
    """
    Used for Function response creation
    """

    def __init__(self, data):
        self.data = data
