import unittest
from app import app

class apiTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] == True
        self.app = app.test_client()

    # Tests a positive user input of type URL for '\encode'.
    # Should return Response Code '200'.
    def test_encode_happy(self):
        test_data = {"url": "https://www.test.com", "encoded": "https://short.est/test"}
        response = self.app.post("/encode", data = test_data)
        self.assertEqual(response.status_code, 200)

    # Tests a negative user input (e.g. NULL value) for '\encode'.
    # Should return Response Code '400'.
    def test_encode_bad(self):
        test_data = None
        response = self.app.post("/encode", data = test_data)
        self.assertEqual(response.status_code, 400)

    # Tests a positive user input of type URL for '\decode'.
    # Should return Response Code '200'.
    def test_decode_happy(self):
        test_data = {"url": "https://www.apple.com", "encoded": "https://short.est/8SUx"}
        response = self.app.post("/decode", data = test_data)
        self.assertEqual(response.status_code, 200)

    # Tests a negative user input (e.g. NULL value) for '\decode'.
    # Should return Response Code '400'.
    def test_decode_bad(self):
        test_data = None
        response = self.app.post("/decode", data = test_data)
        self.assertEqual(response.status_code, 400)

    # Tests an input URL that is not in the database.
    # Should return the string "The entered short URL does not exist. Please try again !"
    def test_decode_not_in_db(self):
        test_data = {"url": "https://www.notindb.com", "encoded": "https://short.est/0000"}
        response = self.app.post("/decode", data = test_data)
        msg = b"The entered short URL does not exist. Please try again !"
        self.assertEqual(response.data, msg)

if __name__ == "__main__":
    unittest.main()