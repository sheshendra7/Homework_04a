import json
import unittest
from unittest.mock import patch, MagicMock
from main import Tester_mind


class TestGit(unittest.TestCase):

    def test_empty_repository(self):
        mock_repository_response = MagicMock(status_code=200)
        mock_repository_response.text = json.dumps([])
        with patch('requests.get', return_value=mock_repository_response):
            self.assertEqual(Tester_mind("Furzi"), 'No repositories created')

    @patch('main.requests')
    def test_get_response(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 2000
        mock_requests.get.return_value = mock_response
        self.assertEqual(Tester_mind('hello'), "Failed to retrieve data!")

    @patch('main.requests')
    def test_tester_mind(self, mock_requests1):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = json.dumps([{'name':'spark-1','commits':2}, {'name':'spark-2','commits':2}])
        mock_requests1.get.return_value = mock_response
        self.assertEqual(Tester_mind('hello'), [('spark-1', 2), ('spark-2', 2)])



if __name__ == '_main_':
    print('Running unit tests')
    unittest.main()