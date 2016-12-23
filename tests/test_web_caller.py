from unittest import TestCase
from requests.exceptions import ConnectionError
from mock import NonCallableMock, patch

from modules.web_caller import get_google, GOOGLE_URL

MOCK_GOOGLE_URL = 'http://not-going-to-work!!!'


class TestWebCaller(TestCase):
    """
    Tests for the `web_caller` module.
    """

    @patch('modules.web_caller.requests.get')
    def test_get_google(self, get):
        """
        Calling `get_google` works as expected.
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

    @patch('modules.web_caller.GOOGLE_URL', MOCK_GOOGLE_URL)
    def test_get_google_with_exception(self):
        """
        Call the `get_google` function while using `patch` to create an
        unreachable URL.

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
