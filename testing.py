import unittest
from app import app

class APItests(unittest.TestCase):
    URL_OBJ = {"encoded": "https://short.est/r3Ca", 
                "url": "https://www.apple.com"}
    def setUp(self):
        app.config['TESTING'] == True
        self.app = app.test_client()

    def test_encode(self):
        response = self.app.post("/encode", json = APItests.URL_OBJ)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()