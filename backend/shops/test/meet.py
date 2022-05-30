from rest_framework.test import APITestCase
from .base import TestBase


class MeetAPITest(APITestCase, TestBase):
    def setUp(self):
        TestBase.__init__(self)

    def test_positive(self):
        url = '/api/v1/meet/+7999999999'
        response = self.client.post(
            url,
            data={
                'pk': self.store.pk,
                'latitude': 1.1,
                'longitude': 1.1
            }
        )
        self.assertEqual(response.status_code, 200, )

    def test_not_enough_keys(self):
        url = '/api/v1/meet/+78005553535'
        response = self.client.post(
            url,
            data={
                'pk': 1,
                'latitude': 1.1,
            }
        )
        self.assertEqual(response.status_code, 400, )

    def test_not_correct_phone_number(self):
        url = '/api/v1/meet/+78005553535'
        response = self.client.post(
            url,
            data={
                'pk': 1,
                'latitude': 1.1,
                'longitude': 1.1
            }
        )
        self.assertEqual(response.status_code, 400, )

    def test_not_such_pk(self):
        url = '/api/v1/meet/+78005553535'
        response = self.client.post(
            url,
            data={
                'pk': 123123,
                'latitude': 1.1,
                'longitude': 1.1
            }
        )
        self.assertEqual(response.status_code, 400, )




