import unittest
import httplib
import urlparse

class RedirectTestCase(unittest.TestCase):
    """
    Test case for testing site redirects
    """

    def redirects(self, source, destination):
        """
        Test domain level redirects
        """
        conn = httplib.HTTPConnection(source)
        conn.request('GET', '/')
        response = conn.getresponse()
        if response.status != 301:
            print response.getheaders()
        self.assertEquals(response.status, 301)
        location = response.getheader('location')
        if location:
            location = urlparse.urlparse(location)
            self.assertEquals(location.netloc, destination)
