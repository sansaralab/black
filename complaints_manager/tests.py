from django.test import TestCase
from complaints_manager import service


class ComplaintsTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_complaint(self):
        service.make_complaint(
            identity='ident!',
            title='pew pew title!',
            content='big content!!',
            category='supa category!'
        )
