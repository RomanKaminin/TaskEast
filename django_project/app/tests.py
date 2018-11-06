import unittest
from app.models import Client, Department
from app.views import ClientDetail, AlphaList


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



class AlphaListTest(unittest.TestCase):

    def test_split_alph_list_one(self):
        objects_alphabet = [ u'А', u'Б', u'В', u'К']
        count_lists = 1
        lists_vals = list(AlphaList.split_alph_list(self, objects_alphabet, count_lists))
        self.assertEqual(lists_vals, [[u'А', u'Б', u'В', u'К']])

    def test_split_alph_list_two(self):
        objects_alphabet = [ u'А', u'Б', u'В', u'Д', u'Е', u'Ё', u'Ж', u'З']
        count_lists = 2
        lists_vals = list(AlphaList.split_alph_list(self, objects_alphabet, count_lists))
        self.assertEqual(lists_vals,
                         [
                             [u'А', u'Б', u'В', u'Д'],
                             [u'Е', u'Ё', u'Ж', u'З']
                         ]
                         )

    def test_split_alph_list_three(self):
        objects_alphabet = [u'Р', u'С', u'Т', u'У', u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Э',]
        count_lists = 3
        lists_vals = list(AlphaList.split_alph_list(self, objects_alphabet, count_lists))
        self.assertEqual(lists_vals,
                         [
                             [u'Р', u'С', u'Т', u'У'],
                             [u'Ф', u'Х', u'Ц', u'Ч'],
                             [u'Ш', u'Щ', u'Э']
                          ]
                         )

    def test_split_alph_list_four(self):
        objects_alphabet = [
            u'Д', u'Е', u'Ё', u'Ж',
            u'З', u'И', u'К', u'Л',
            u'Ф', u'Х', u'Ц', u'Ч',
            u'Ш', u'Щ', u'Ы', u'Ъ'
        ]
        count_lists = 4
        lists_vals = list(AlphaList.split_alph_list(self, objects_alphabet, count_lists))
        self.assertEqual(lists_vals,
                         [
                             [u'Д', u'Е', u'Ё', u'Ж'],
                             [u'З', u'И', u'К', u'Л'],
                             [u'Ф', u'Х', u'Ц', u'Ч'],
                             [u'Ш', u'Щ', u'Ы', u'Ъ']
                          ]
                         )

    def test_split_alph_list_five(self):
        objects_alphabet = [
            u'Д', u'Е', u'Ё', u'Ж',
            u'З', u'И', u'К', u'Л',
            u'М', u'Н', u'О', u'П',
            u'Ф', u'Х', u'Ц', u'Ч',
            u'Ш', u'Щ', u'Ы', u'Ъ',
            u'Ь', u'Э'
        ]
        count_lists = 5
        lists_vals = list(AlphaList.split_alph_list(self, objects_alphabet, count_lists))
        self.assertEqual(lists_vals,
                         [
                             [u'Д', u'Е', u'Ё', u'Ж', u'З'],
                             [u'И', u'К', u'Л', u'М', u'Н'],
                             [u'О', u'П', u'Ф', u'Х'],
                             [u'Ц', u'Ч', u'Ш', u'Щ'],
                             [u'Ы', u'Ъ', u'Ь', u'Э']
                          ]
                         )

    def test_split_alph_list_six(self):
        objects_alphabet = [
            u'А', u'Б', u'В', u'Г',
            u'Д', u'Е', u'Ё', u'Ж',
            u'З', u'И', u'К', u'Л',
            u'М', u'Н', u'О', u'П',
            u'Ф', u'Х', u'Ц', u'Ч',
            u'Ш', u'Щ', u'Ы', u'Ъ',
            u'Ь', u'Э', u'Ю', u'Я'
        ]
        count_lists = 6
        lists_vals = list(AlphaList.split_alph_list(self, objects_alphabet, count_lists))
        self.assertEqual(lists_vals,
                         [
                             [u'А', u'Б', u'В', u'Г', u'Д'],
                             [u'Е', u'Ё', u'Ж', u'З', u'И'],
                             [u'К', u'Л', u'М', u'Н', u'О'],
                             [u'П', u'Ф', u'Х', u'Ц', u'Ч'],
                             [u'Ш', u'Щ', u'Ы', u'Ъ'],
                             [u'Ь', u'Э', u'Ю', u'Я']
                         ]
                         )

    def test_split_alph_list_seven(self):
        objects_alphabet = [
            u'А', u'Б', u'В', u'Г',
            u'Д', u'Е', u'Ё', u'Ж',
            u'З', u'И', u'Й', u'К',
            u'Л', u'М', u'Н', u'О',
            u'П', u'Р', u'С', u'Т',
            u'У', u'Ф', u'Х', u'Ц',
            u'Ч', u'Ш', u'Щ', u'Ъ',
            u'Ы', u'Ь', u'Э', u'Ю',
            u'Я'
        ]
        count_lists = 7
        lists_vals = list(AlphaList.split_alph_list(self, objects_alphabet, count_lists))
        self.assertEqual(lists_vals,
                         [
                             [u'А', u'Б', u'В', u'Г', u'Д'],
                             [u'Е', u'Ё', u'Ж', u'З', u'И'],
                             [u'Й', u'К', u'Л', u'М', u'Н'],
                             [u'О', u'П', u'Р', u'С', u'Т'],
                             [u'У', u'Ф', u'Х', u'Ц', u'Ч'],
                             [u'Ш', u'Щ', u'Ъ', u'Ы'],
                             [u'Ь', u'Э', u'Ю', u'Я']
                         ]
                         )


