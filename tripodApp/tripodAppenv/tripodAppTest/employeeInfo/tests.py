from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .models import EmployeeInfo


# Create your tests here.

def test_home_page_status_code(self):
    response = self.client.get('/')
    self.assertEquals(response.status_code, 200)


class EmployeeInfoTests(TestCase):

    @classmethod
    def setUp(cls):
        EmployeeInfo.objects.create(name='praise')

    def test_text_content(self):
        employeeInfo = EmployeeInfo.objects.get(id=1)
        expected_object_name = f'{employeeInfo.name}'
        self.assertEquals(expected_object_name, 'praise')

