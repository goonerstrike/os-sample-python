import unittest
import requests

class TestFlask(unittest.TestCase):
  def test_top_tweets(self):
    r = requests.get("http://127.0.0.1:5000/top_tweets")
    page_src = r.text

    if page_src.find("Hello World") < 0:
      self.fail("Cannot find hello world")


