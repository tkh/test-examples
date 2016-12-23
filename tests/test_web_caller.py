from unittest import TestCase
from mock import NonCallableMock, patch

from modules.web_caller import get_google, GOOGLE_URL


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
