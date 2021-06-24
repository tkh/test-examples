from random import randint


SERVICE_URL = 'service://example.com/api'


class ServiceError(Exception):
    """
    Sometimes things do not always go as planned.
    """


class ImaginaryServiceConnection:
    """
    An imaginary connection to an imaginary service.
    """

    def __init__(self, username, password):
        """
        Establish the imaginary connection and return something nice.
        """

        self.username = username
        self.password = password
        self.service_url = SERVICE_URL

    def call(self, function_name, *args, **kwargs):
        """
        Send back a random result to keep everyone happy.
        """

        if function_name == 'fail':
            raise ServiceError('Call failed!')

        return randint(
            len(args) if args else 1,
            len(kwargs) if kwargs else 1000,
        )


class ServiceClient:
    """
    Provides access to an imaginary service.
    """

    def __init__(self, username, password):
        self.connection = self._get_connection(username, password)

    def _get_connection(self, username, password):
        """
        Establish a connection to the imaginary service.
        """

        return ImaginaryServiceConnection(username, password)

    def call_remote_function(self, function_name, *args, **kwargs):
        """
        Call a remote function by name with the given args and kwargs.
        """

        return self.connection.call(function_name, *args, **kwargs)
