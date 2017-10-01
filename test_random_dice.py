import unittest

import truerandomdice.ranclient


class TestRanClient(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_test_connection_with_invalid_api_key(self):
        result = truerandomdice.ranclient.test_connection('invalid')
        self.assertEqual(False, result)
