from unittest import mock
from unittest.mock import MagicMock

import os
import sendgrid.helpers.inbound.app as App
from sendgrid.helpers.inbound.app import app
from sendgrid.helpers.inbound.config import Config

try:
    import unittest2 as unittest
except ImportError:
    import unittest

class AppTest(unittest.TestCase):

    def setUp(self):
        App.app = app.test_client(self)
        App.app.run = MagicMock()
        App.config.debug = True

    @mock.patch.dict(os.environ, {'PORT': '5001'})
    def test_main_no_debug(self):
        App.main()
        self.assertFalse(App.config.debug)
        self.assertTrue(App.app.run.called)

    @mock.patch.dict(os.environ, {'PORT': '5000'})
    def test_main_debug(self):
        App.main()
        self.assertTrue(App.config.debug)
        self.assertTrue(App.app.run.called)

    def test_get_home(self):
        response = App.app.get('/')
        self.assertEqual(response.status_code, 200)



