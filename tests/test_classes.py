from unittest import TestCase
from mock import patch

from modules.classes import (
    ImaginaryServiceConnection,
    ServiceClient,
    ServiceError,
)


class TestImaingaryServiceConnection(TestCase):
    """
    Tests for the `modules.classes.ImaginaryServiceConnection` class.
    """

    @patch('modules.classes.SERVICE_URL', 'something-else')
    def test_instantiation(self):
        """
        Instantiation of ImaginaryServiceConnection works as expected.
        """

        isc = ImaginaryServiceConnection('username', 'password')

        # Instantiating the class should assign the expected class attributes
        self.assertEqual('username', isc.username)
        self.assertEqual('password', isc.password)
        self.assertEqual('something-else', isc.service_url)

    def test_call(self):
        """
        `ImaginaryServiceConnection.call` works as expected.
        """

        isc = ImaginaryServiceConnection('username', 'password')

        # Calling the `.call` function should return an integer
        result = isc.call('function', 'a', 'b', {'c': 1, 'd': 2})
        self.assertIsInstance(result, int)

    def test_call_with_known_exception(self):
        """
        `ImaginaryServiceConnection.call` raises `ServiceError` as expected.
        """

        isc = ImaginaryServiceConnection('username', 'password')

        # Calling the `.call` function with 'fail' should raise ServiceError
        with self.assertRaises(ServiceError):
            isc.call('fail', 'a', 'b', {'c': 1, 'd': 2})

    @patch('modules.classes.ImaginaryServiceConnection.call')
    def test_call_with_simulated_exception(self, call):
        """
        `ImaginaryServiceConnection.call` raises `ServiceError` as expected
        with simulated error.
        """

        call.side_effect = ServiceError('Simulated error')

        isc = ImaginaryServiceConnection('username', 'password')

        # Calling the `.call` function should return the simulated error
        with self.assertRaises(ServiceError):
            isc.call('fail', 'a', 'b', {'c': 1, 'd': 2})


class TestServiceClient(TestCase):
    """
    Tests for the `modules.classes.ServiceClient` class.
    """

    def test_instantiation(self):
        """
        Instantiation of `ServiceClient` works as expected.
        """

        sc = ServiceClient('username', 'password')

        # Instantiating the class should create the `connection` attribute on
        # the instance using ImaginaryServiceConnection
        self.assertIsInstance(sc.connection, ImaginaryServiceConnection)

    def test_call_remote_function(self):
        """
        ServiceClient.call_remote_function works as expected.
        """

        sc = ServiceClient('username', 'password')
        result = sc.call_remote_function(
            'some_function',
            'a', 'b',
            {'c': 1, 'd': 2},
        )
        # Should receive an integer back
        self.assertIsInstance(result, int)

    @patch('modules.classes.ImaginaryServiceConnection.call')
    def test_call_remote_function_with_mocks(self, call):
        """
        ServiceClient.call_remote_function works as expected while mocking
        `ImaginaryServiceConnection.call`.
        """

        # Set up the mock `.call` response for
        # `ImaginaryServiceConnection.call`
        call.return_value = 'result'

        sc = ServiceClient('username', 'password')
        result = sc.call_remote_function(
            'some_function',
            'a', 'b',
            {'c': 1, 'd': 2},
        )

        # Should receive 'result' back
        self.assertEqual(call.return_value, result)

    @patch('modules.classes.ImaginaryServiceConnection.call')
    def test_call_remote_function_with_error(self, call):
        """
        ServiceClient.call_remote_function raises `ServiceError` as expected
        when an error is encountered via `ImaginaryServiceConnection.call`
        """

        # Set up the error encountered during call to
        # `ImaginaryServiceConnection.call`
        call.side_effect = ServiceError('Something bad!')

        sc = ServiceClient('username', 'password')

        # `ServiceError` is raised when calling
        # `ServiceClient.call_remote_function`
        with self.assertRaises(ServiceError):
            sc.call_remote_function(
                'some_function',
                'a', 'b',
                {'c': 1, 'd': 2},
            )
