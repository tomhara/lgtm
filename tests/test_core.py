import unittest

class LgtmTest(unittest.TestCase):
    def test_lgtm(self):
        from python_jissen.core import lgtm
        self.assertIsNone(lgtm())