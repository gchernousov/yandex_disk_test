import unittest
from parameterized import parameterized

from main import create_folder, get_folder_info


class TestYandex(unittest.TestCase):

    def setUp(self) -> None:
        print(">>> setUp")

    def tearDown(self) -> None:
        print(">>> tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print(">>> setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print(">>> tearDownClass")


    # Тестируем создание папки:
    # 1) Создаем папку test_folder_1, которой еще нет, ожидаем status code 200
    # 2) Создаем папку Folder_A, которая уже есть, ожидаем status code 409
    @parameterized.expand(
        [
            ("test_folder_1", 201),
            ("Folder_A", 409)
        ]
    )
    def test_create_folder(self, folder_name, response):
        self.assertEqual(create_folder(folder_name), response)


    # Тестируем получение информации о папке:
    # 1) Папки test_folder_x у нас нет, ожидаем не 200, а 404
    # 2) Папка Folder_A у нас есть, ожидаем не 404
    @parameterized.expand(
        [
            ("test_folder_x", 200, 404),
            ("Folder_A", 404, 200)
        ]
    )
    def test_get_folder_info(self, folder_name, res1, res2):
        result = get_folder_info(folder_name).status_code
        self.assertNotEqual(result, res1)
        self.assertEqual(result, res2)


    # def test_create_folder_2(self):
    #     self.assertEqual(create_folder("test_folder_99"), 201)
    #     self.assertEqual(create_folder("test_folder_99"), 409)