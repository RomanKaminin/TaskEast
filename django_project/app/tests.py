import unittest
from app.models import Client, Department

# class ClientTestCase(unittest.TestCase):
#     def setUp(self):
#         self.ioan = Client.objects.create(
#             username="Иван",
#             first_name="Иванов",
#             last_name="Иванович",
#             born_date="2000-10-10",
#             email="ivan@mail.ru",
#             start_work_date="2018-10-1",
#             end_work_date=None,
#             position="Программист",
#             department="ИТ",
#
#         )
#         self.den = Client.objects.create(
#             username="денис",
#             first_name="денисов",
#             last_name="денисович",
#             born_date="2000-10-20",
#             email="ivan@mail.ru",
#             start_work_date="2018-10-1",
#             end_work_date="2018-10-10",
#             position="Бухгалтер",
#             department="Бухгалтерия",
#
#         )
MODELS = [Client, Department]

class CoreModelTest(unittest.TestCase):
    "Test the models contained in the 'core' app."
    def setUp(self):
        'Populate test database with model instances.'
        self.client = Client()
    def tearDown(self):
        'Depopulate created model instances from test database.'
        for model in MODELS:
            for obj in model.objects.all():
                obj.delete()
    def test_something(self):
        "This is a test for something."
        self.assertEquals(True, 1)
