from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from ..models import Employee, Store


class TestBase:
    def __init__(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            username='admin',
            password='admin',
            email='test@test.com',
        )
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(
            name='Тестовый юзер',
            phone_number='+7999999999'
        )
        self.store = Store.objects.create(
            name='Магазин',
            employee=self.employee
        )

