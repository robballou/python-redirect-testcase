import unittest
from redirect_testcase import RedirectTestCase

class ExampleRedirectTest(RedirectTestCase):
    """
    Sample test

    Note that this test will actually fail (it doesn't redirect, so .redirects() will
    not pass).
    """
    def test_redirect(self):
        self.redirects('www.example.com', 'example.com')

if __name__ == '__main__':
    unittest.main()
