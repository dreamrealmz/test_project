from rest_framework.test import APITestCase
from .base import TestBase


class StoreAPITest(APITestCase, TestBase):
    def setUp(self):
        TestBase.__init__(self)

    def test_positive(self):
        url = '/api/v1/stores/+7999999999'
        response = self.client.get(
            url,
        )
        self.assertEqual(response.status_code, 200, )

    def test_negative(self):
        url = '/api/v1/stores/+123'
        response = self.client.get(
            url,
        )
        self.assertEqual(response.status_code, 200, )
        self.assertIs(len(response.json()['stores']), 0)





