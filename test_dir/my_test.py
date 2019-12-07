import json
from urllib import request

from django.test import TestCas


class CurrenciesAPITestCase(TestCase):
  
    def setUp(self):
        self.url = 'http://www.nbrb.by/api/exrates/currencies'

    def test_currencies_api_structure(self):
        """Test Currencies API data structure"""
        req = request.urlopen(self.url)
        resp = req.read().decode()
        resp_json = json.loads(resp)
        
        # TODO: Implement checks
        # self.assertIsInstance(resp_json, dict)
