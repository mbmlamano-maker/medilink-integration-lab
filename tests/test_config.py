import os
import unittest
from unittest import mock

import config


class ConfigTests(unittest.TestCase):
    def test_api_key_is_read_from_environment(self):
        with mock.patch.dict(os.environ, {"MEDILINK_API_KEY": "injected-value"}):
            self.assertEqual(config.get_api_key(), "injected-value")

    def test_api_key_falls_back_to_local_default(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertEqual(config.get_api_key(), "local-demo-key")

    def test_api_key_is_available_as_non_empty_string(self):
        # Checks presence/type only; never prints or compares the real secret.
        self.assertTrue(config.get_api_key().strip())

    def test_timeout_default_is_positive_integer(self):
        with mock.patch.dict(os.environ, {}, clear=True):
            self.assertGreater(config.get_request_timeout(), 0)

    def test_timeout_is_read_from_environment(self):
        with mock.patch.dict(os.environ, {"REQUEST_TIMEOUT": "9"}):
            self.assertEqual(config.get_request_timeout(), 9)

    def test_timeout_must_be_greater_than_zero(self):
        for bad in ("0", "-3"):
            with mock.patch.dict(os.environ, {"REQUEST_TIMEOUT": bad}):
                with self.assertRaises(ValueError):
                    config.get_request_timeout()


if __name__ == "__main__":
    unittest.main()
