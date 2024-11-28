import unittest

import sys
sys.path.append('C:/Users/$MNH400-P2NKHD8RVQGL/Desktop/python_labs')

from unittest.mock import patch, MagicMock
from classes.requestClasses.GetRequest import GetRequest
from classes.requestClasses.APIRequestFactory import APIRequestFactory
from classes.requestClasses.RequestSettings import RequestSettings

from shared.functions.errorFunctions import isValidUrl

class TestAPIRequestFactory(unittest.TestCase):

    def setUp(self):
        self.settings = RequestSettings()
        self.factory = APIRequestFactory(self.settings)
        self.test_url = 'https://official-joke-api.appspot.com/jokes/programming/ten'
        self.test_result = {"ip": "178.92.191.97"}

    def test_create_request_get(self):
        request = self.factory.create_request(self.factory)
        self.assertIsInstance(request, GetRequest)

    @patch('requests.get')
    def test_send_request(self, mock_get):
        """Тестуємо, чи правильно працює метод send для запиту"""
        mock_response = MagicMock()
        mock_response.json.return_value = self.test_result
        mock_get.return_value = mock_response

        # Виконуємо запит
        request = self.factory.create_request(self.factory)
        response_data = request.send()

        # Перевіряємо, чи був викликаний requests.get
        mock_get.assert_called_once_with(self.test_url)

        # Перевіряємо результат
        self.assertEqual(response_data, self.test_result)

    @patch('builtins.input', side_effect=["4", "https://custom-api.com/data"])
    def test_set_url_option_4_custom_url(self, mock_input):
        settings = RequestSettings()
        result = settings.setUrl()  # Викликаємо метод setUrl

        # Перевіряємо, чи метод повернув True, що означає, що URL встановлено успішно
        self.assertTrue(result)

        # Перевіряємо, чи URL був встановлений на введений користувачем
        self.assertEqual(settings.url, "https://custom-api.com/data")

    def test_valid_url_http(self):
        url = "http://example.com"
        self.assertTrue(isValidUrl(url))

        url = "123"
        self.assertFalse(isValidUrl(url))

if __name__ == '__main__':
    unittest.main()
