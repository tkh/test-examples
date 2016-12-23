from unittest import TestCase

from modules.web_caller import get_google


class TestWebCaller(TestCase):
    """
    Tests for the `web_caller` module.
    """

    def test_get_google(self):
        """
        Calling `get_google` works as expected.
        """

        response = get_google()
        self.assertEqual(200, response.status_code)
