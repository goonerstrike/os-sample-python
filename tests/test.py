import unittest
import requests

class TestFlask(unittest.TestCase):
  def test_hello_world(self):
    r = requests.get("http://127.0.0.1:8080/")
    page_src = r.text

    if page_src.find("Hello World") < 0:
      print("BLEH")
      self.fail("Cannot find Hello World")

if __name__ == "__main__":
    unittest.main(warnings='ignore', failfast = True)
