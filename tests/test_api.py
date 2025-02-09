import unittest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app
from app.routes import add_data  

class TEST_API_ENDPOINT(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)   # FastAPI test client

        self.valid_data = {  # Valid stockdata testcase
            'id': 1,
            'datetime': "2025-01-01T00:00:00",
            'open': "100.5",
            'high': "105.0",
            'low': "99.0",
            'close': "102.5",
            'volume': 1000000
        }

        self.invalid_data_missing_field = {  # missing field testcase
            'datetime': "2025-01-01T00:00:00",
            'high': "105.0",
            'low': "99.0",
            'close': "102.5",
            'volume': 1000000
        }

        self.invalid_data_wrong_type = {  # open test case if its string or not
            'datetime': "2025-01-01T00:00:00",
            'open': "invalid_value",
            'high': "105.0",
            'low': "99.0",
            'close': "102.5",
            'volume': 1000000
        }
    #was connecting to db causing error thats why used mock call
    @patch("app.routes.prisma", new_callable=AsyncMock)   
    def test_valid_data(self, mock_prisma):
        mock_prisma.stockprice.create.return_value = self.valid_data
        response = self.client.post("/data", json=self.valid_data)
        self.assertEqual(response.status_code, 200)  

    def test_invalid_data_missing_field(self):
        response = self.client.post('/data', json=self.invalid_data_missing_field)
        self.assertEqual(response.status_code, 422)  

    def test_invalid_data_wrong_type(self):
        response = self.client.post("/data", json=self.invalid_data_wrong_type)
        self.assertEqual(response.status_code, 422) 

if __name__ == "__main__":
    unittest.main()
