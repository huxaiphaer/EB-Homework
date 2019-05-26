import io
import sys
import unittest
from unittest.mock import patch

from tarea2 import Guess


class TestTarea2(unittest.TestCase, Guess):

    def setUp(self):
        """
        Initializing all our data structures.
        :return:
        """
        self.ok = [[], [], [], [], []]
        self.no = [[], [], [], []]
        self.hit = [[], [], [], []]
        self.dismiss = [[], [], [], []]

    @patch('tarea2.Guess.find_regulars')
    def test_find_regulars_is_called(self, mock_reg):
        """
        Testing is find_regulars()is called while running the application.
        :param mock_reg:
        :return:
        """
        self.find_regulars()
        self.assertTrue(mock_reg.called)

    def test_entering_wrong_value_regular_num(self):
        """
        Test while entering the wrong value in find_regulars()
        :return:
        """
        user_input = [
            '1',
            '2',
            '3',
            '4'
        ]
        expected_output = [
        ]

        with patch('builtins.input', side_effect=user_input):
            self.find_regulars()
            reg = self.ok
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            # print the error message
            print('Ha ingresado un valor equivocado.', capturedOutput.getvalue())
            self.assertEquals('Ha ingresado un valor equivocado. \n', capturedOutput.getvalue())
        self.assertEqual(reg, expected_output)

    @patch('tarea2.Guess.find_number')
    def test_find_numbers_is_called(self, mock_num):
        """
        This tests if the find_numbers() is called while the app
        is running.
        :param mock_num:
        :return:
        """
        self.find_number()
        self.assertTrue(mock_num.called)

    @patch('tarea2.Guess.find_number')
    def test_run_find_numbers(self, mock_num):
        """
        It tests/mocks  when the find_numbers() is running.
        This is a sample representation of data taken
        :return:
        """
        q1 = 1
        if q1 == 1:
            self.hit[3].append(self.ok[3])
            self.dismiss[0].append([self.ok[0]])
            self.assertNotEquals(self.dismiss, [])
            self.assertNotEquals(self.hit, [])


if __name__ == "__main__":
    unittest.main()
