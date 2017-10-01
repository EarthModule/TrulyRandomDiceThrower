import Queue
import time
import unittest

import rdoclient

import truerandomdice.ranclient
import truerandomdice.set_api_key


class TestRanClient(unittest.TestCase):
    api_key = None

    def setUp(self):
        file = open("api_key_for_tests.txt", "r")
        apikey = file.read()
        self.api_key = apikey
        file.close()

    def test_test_connection_with_invalid_api_key(self):
        result = truerandomdice.ranclient.test_connection('invalid')
        self.assertEqual(False, result)

    def test_test_connection_with_valid_api_key(self):
        result = truerandomdice.ranclient.test_connection(self.api_key)
        self.assertEqual(True, result)

    def test_capacity_left(self):
        reqs, bits = truerandomdice.ranclient.get_capacity_left(self.api_key)
        self.assertGreater(reqs, 0)
        self.assertGreater(bits, 0)

    def test_capacity_left_with_invalid_api_key(self):
        try:
            result = truerandomdice.ranclient.get_capacity_left('invalid')
        except ValueError:
            self.assertTrue(True)

    def test_has_capacity(self):
        has_capacity = truerandomdice.ranclient.has_capacity(self.api_key)
        self.assertEqual(True, has_capacity)

    def test_has_capacity_with_invalid_api_key(self):
        try:
            has_capacity = truerandomdice.ranclient.has_capacity('invalid')
        except ValueError:
            self.assertTrue(True)

    def test_initialize_client_with_live_results(self):
        client, cache = truerandomdice.ranclient.initialize_client(self.api_key, live_results=True)
        self.assertTrue(client, isinstance(client, rdoclient.RandomOrgClient))
        self.assertEqual(cache, None)

    def test_initialize_client_with_cache(self):
        client, cache = truerandomdice.ranclient.initialize_client(self.api_key, cached=True, cache_size=10,
                                                                   cache_min=1, cache_max=10)
        self.assertTrue(client, isinstance(client, rdoclient.RandomOrgClient))
        success = False
        arr = None
        while success is not True:
            try:
                arr = cache.get()
                success = True
            except Queue.Empty:
                time.sleep(0.1)

        self.assertEqual(len(arr), 10)

    def test_initialize_client_with_custom_timeouts(self):
        client, cache = truerandomdice.ranclient.initialize_client(self.api_key, blocking_timeout=5, http_timeout=5)
        self.assertTrue(client, isinstance(client, rdoclient.RandomOrgClient))
