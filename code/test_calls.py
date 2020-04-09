import unittest
import requests
from code import calls
import io
from mock import Mock, patch


class TestCalls(unittest.TestCase):

    def test_get_data_no_mock(self):
        assert calls.get_data() == 200

    def test_get_data_mock(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            assert calls.get_data() == 200

    @patch('builtins.open')
    def test_give_advice_format_check_decorated(self, mock_open):
        fake_file = io.StringIO('Sam\nDan\n')
        mock_open.return_value = fake_file
        result = calls.give_advice('/limit/does/not/exist')
        self.assertEqual('Flatten the curve!\n'
                         'Sam, be sure to wash your hands!\n'
                         'Dan, be sure to wash your hands!\n',
                         result)


if __name__ == '__main__':
    unittest.main()
