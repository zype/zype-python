__author__ = "Khurshid Fayzullaev"

import os
from ConfigParser import SafeConfigParser
from unittest import TestCase
from nose.tools import raises

from zype import Zype


class TestClient(TestCase):

    def setUp(self):
        config = SafeConfigParser()
        config.read(os.path.join(os.path.abspath(
            os.path.dirname(__file__)), '', 'config.ini'))
        self.api_key = config.get("KEYS", "APIKey")
        self.app_key = config.get("KEYS", "APPKey")

    @raises(ValueError)
    def test_only_one_auth_type(self):
        client = Zype(
            api_key=self.api_key, app_key=self.app_key)

    def test_get_all_videos_api_key(self):
        client = Zype(
            api_key=self.api_key)
        videos = client.get("videos")
        self.assertIsNotNone(videos)

    def test_get_all_videos_app_key(self):
        client = Zype(
        app_key=self.app_key)
        videos = client.get("videos")
        self.assertIsNotNone(videos)

    def tearDown(self):
        self.api_key = ""
