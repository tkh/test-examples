from unittest import TestCase
from requests.exceptions import ConnectionError
from mock import NonCallableMock, patch

from modules.web_caller import get_google, GOOGLE_URL

MOCK_GOOGLE_URL = 'http://not-going-to-work!!!'


class TestWebCallerSimple(TestCase):
    """
    Simple tests for the `web_caller` module.
    """

    @patch('modules.web_caller.requests.get')
    def test_get_google(self, get):
        """
        Call `get_google` using `patch` to override the requests.get function
        in order to make assertions about what happened and verify the expected
        result.
        """

        # Create a mock response
        mock_response = NonCallableMock(
            status_code=200,
        )
        # Assign the mock response as the requests.get return value
        get.return_value = mock_response

        # Call the function
        response = get_google()

        # Check that requests.get was called with the expected URL
        get.assert_called_once_with(GOOGLE_URL)

        # Check that the mock response is returned
        self.assertIs(mock_response, response)

        # Check that the mocked response.status_code is as expected
        self.assertEqual(200, response.status_code)


class TestWebCallerWithExceptions(TestCase):
    """
    Tests for the `web_caller` module with exception assertions.
    """

    @patch('modules.web_caller.GOOGLE_URL', MOCK_GOOGLE_URL)
    def test_get_google_with_exception(self):
        """
        Call the `get_google` function while using `patch` on a module
        variable to create an unreachable URL.

        Assert that the error happened and capture it using assertRaises.
        """

        # Call the function via assertRaises and confirm the exception is
        # raised by making the call
        self.assertRaises(ConnectionError, get_google)

    @patch('modules.web_caller.GOOGLE_URL', MOCK_GOOGLE_URL)
    def test_get_google_with_exception_context_manager(self):
        """
        Call the `get_google` function while using `patch` to create an
        unreachable URL.

        Assert that the error happened and capture it using the assertRaises
        context manager.
        """

        # Establish an assertRaises context manager
        with self.assertRaises(ConnectionError):
            # Call the function
            get_google()

    @patch('modules.web_caller.requests.get')
    def test_get_google_with_mock_driven_exception(self, get):
        """
        Call the `get_google` function while using `patch` to create an
        unreachable URL.
        """

        # Assign a side_effect of requests.exceptions.ConnectionError to the
        # patched requests.get function to simulate an excepion being raised
        get.side_effect = ConnectionError('Error!')

        # Establish an assertRaises context manager
        with self.assertRaises(ConnectionError):
            # Call the function
            get_google()

        # Check that requests.get was called as expected
        get.assert_called_once_with(GOOGLE_URL)
