import unittest
from app.models import Client, Department
from app.views import ClientDetail


class ClientModelTest(unittest.TestCase):
    def create_client_depart(self):
        self.managers = Department.objects.create(
            name="Менеджеры",
            parent=None,
        )
        self.client = Client.objects.create(
            username="Иван",
            first_name="Иванов",
            last_name="Иванович",
            born_date="2000-10-10",
            email="ivan@mail.ru",
            start_work_date="2018-10-1",
            end_work_date=None,
            position="2018-10-30",
            department=self.managers,
        )
        return self.client

    def test_client_model_creation(self):
        new_client = self.create_client_depart()
        self.assertTrue(isinstance(new_client, Client))

    def test_client_detail_view(self):
        new_client = self.create_client_depart()
        view = ClientDetail()
        view.kwargs = dict(pk=new_client.id)
        self.assertEqual(view.get_queryset(), new_client)