import os
import unittest
from unittest import mock

from sendgrid.helpers.inbound.config import Config
from sendgrid.helpers.inbound.app import app, debug_enabled


class UnitTests(unittest.TestCase):

    def setUp(self):
        self.config = Config()
        app.testing = True
        self.tester = app.test_client(self)

    def test_up_and_running(self):
        response = self.tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_used_port_true(self):
        if self.config.debug_mode:
            port = int(os.environ.get("PORT", self.config.port))
            self.assertEqual(port, self.config.port)

    def test_debug_disabled_by_default(self):
        self.assertFalse(debug_enabled(self.config, self.config.port))

    def test_debug_disabled_on_platform_port(self):
        cfg = mock.Mock(debug_mode=True, port=5000)
        self.assertFalse(debug_enabled(cfg, 34567))

    def test_debug_disabled_in_prod(self):
        cfg = mock.Mock(debug_mode=True, port=5000)
        with mock.patch.dict(os.environ, {'ENV': 'prod'}):
            self.assertFalse(debug_enabled(cfg, 5000))

    def test_debug_enabled_locally_when_opted_in(self):
        cfg = mock.Mock(debug_mode=True, port=5000)
        with mock.patch.dict(os.environ, {'ENV': 'dev'}):
            self.assertTrue(debug_enabled(cfg, 5000))
