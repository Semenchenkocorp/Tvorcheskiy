import unittest
import pandas as pd
from ddwdwd import process_csv_file, send_email

class TestProcessCSVFile(unittest.TestCase):

    def setUp(self):
        # Создание тестового файла
        self.test_path = 'test.csv'
        data = {
            'platform': ['vk', 'vk', 'fb', 'fb', 'ok', 'ok'],
            'event': ['view', 'click', 'view', 'click', 'view', 'click']
        }
        df = pd.DataFrame(data)
        df.to_csv(self.test_path, index=False)

        # Ожидаемый результат
        self.expected_data = pd.DataFrame({
            'platform': ['fb', 'ok', 'vk'],
            'views': [1, 1, 1],
            'clicks': [1, 1, 1]
        })

    def test_process_csv_file(self):
        # Проверяем эквивалентность файлов
        result_data = process_csv_file(self.test_path)
        pd.testing.assert_frame_equal(result_data, self.expected_data)

    def delete_test_file(self):
        # Удаление тестового файла
        import os
        os.remove(self.test_path)

class TestSendEmail(unittest.TestCase):

    def setUp(self):
        # Тестовые данные
        self.email = 'ngusev071@gmail.com'
        self.password = 'zrcgjifbpgojohyk'
        self.recipient = 'semenchenkocorp@mail.ru'
        self.data = pd.DataFrame({
            'platform': ['fb', 'ok', 'vk'],
            'views': [1, 1, 1],
            'clicks': [1, 1, 1]
        })

    def test_send_email(self):
        # Проверка отправки сообщения
        send_email(self.email, self.password, self.recipient, self.data)