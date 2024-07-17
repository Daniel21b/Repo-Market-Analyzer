import unittest
from app import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_repo_market_post(self):
        response = self.app.post('/api/repo-market', json={
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "bank": "Bank A",
            "loan_amount": 1000000.0
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('interest_rate_prediction', response.json)
        self.assertIn('market_analysis', response.json)
        self.assertIn('risk_assessment', response.json)

if __name__ == '__main__':
    unittest.main()
