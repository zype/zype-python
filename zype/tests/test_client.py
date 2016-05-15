import os
from ConfigParser import SafeConfigParser
from unittest import TestCase
from zype import Zype


class TestClient(TestCase):

    def setUp(self):
        config = SafeConfigParser()
        config.read(os.path.join(os.path.abspath(
            os.path.dirname(__file__)), '', 'config.ini'))
        self.api_key = config.get("KEYS", "APIKey")

    def test_get_all_videos(self):
        client = Zype(
            api_key=self.api_key)
        videos = client.get("videos")
        self.assertIsNotNone(videos)

    def tearDown(self):
        self.api_key = ""
