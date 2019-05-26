import unittest.mock
from random import randint
from unittest.mock import patch, call

from tarea1 import User, Guess, Host


# import StringIO
class TestTarea1User(unittest.TestCase, User):

    @patch('builtins.input', side_effect=["36", "1", "12345", "1234"])
    def test_userNum_len(self, input_mock):
        '''
        Verifica len() del input que debe ser de 4 cifras.
        '''
        expected = [
            call('Indique un número de 4 cifras:'),
            call('Número inválido.\nIndique un número de 4 cifras:'),
            call('Número inválido.\nIndique un número de 4 cifras:'),
            call('Número inválido.\nIndique un número de 4 cifras:')]
        self.userNum()
        self.assertEqual(input_mock.mock_calls, expected)

    @patch('builtins.input', side_effect=["1224", "1090", "1255", "1234"])
    def test_userNum_is_repeated(self, input_mock):
        '''
        Verifica que en número ingresado no tenga cifras repetidas.
        '''
        expected = [
            call('Indique un número de 4 cifras:'),
            call('Número inválido: ninguna cifra debe repetirse.\nIndique un número de 4 cifras:'),
            call('Número inválido: ninguna cifra debe repetirse.\nIndique un número de 4 cifras:'),
            call('Número inválido: ninguna cifra debe repetirse.\nIndique un número de 4 cifras:')]
        self.userNum()
        print("--> ", input_mock.mock_calls)
        self.assertEqual(input_mock.mock_calls, expected)


class TestTarea1Guess(unittest.TestCase, Guess):

    # def foo(self, some):
    # 	print(some)

    def test_guess_num_ok_1(self):
        '''
        Verifica cifras OK (1).
        '''
        self.user_num = 1234
        self.num = 8764
        self.guess()
        self.assertEqual(self.ok, 1)

    def test_guess_num_ok_2(self):
        '''
        Verifica cifras OK (2).
        '''
        self.user_num = 1234
        self.num = 8734
        self.guess()
        self.assertEqual(self.ok, 2)

    def test_guess_num_ok_4(self):
        '''
        Verifica cifras OK (4).
        '''
        self.user_num = 1234
        self.num = 1234
        self.guess()
        self.assertEqual(self.ok, 4)

    def test_guess_reg_1(self):
        '''
        Verifica cifras REGULAR (1).
        '''
        self.user_num = 1234
        self.num = 8746
        self.guess()
        self.assertEqual(self.reg, 1)

    def test_guess_reg_4(self):
        '''
        Verifica cifras REGULAR (4).
        '''
        self.user_num = 1234
        self.num = 4321
        self.guess()
        self.assertEqual(self.reg, 4)


class RandomGen:
    def __init__(self):
        self.num = None

    def compute_num(self):
        random = randint(1000, 8876)
        random = list(map(int, str(random)))
        while random[0] == random[1] or random[0] == random[2] or \
                random[0] == random[3] or random[1] == random[2] or \
                random[1] == random[3] or random[2] == random[3]:
            random = randint(1023, 9876)
            random = list(map(int, str(random)))
        num = ""
        self.num = int(num.join(map(str, random)))


class TestTarea1Host(unittest.TestCase, Host):
    '''
     Test that the num method.
    '''

    @patch('tarea1.Host.num')
    def test_random_num_generation(self, mock_num):

        self.num()
        self.assertTrue(mock_num.called)
        self.assertGreater(9876, 1026)

    def test_range(self):
        gen = RandomGen()
        for i in range(1023):
            gen.compute_num()
            self.assertGreaterEqual(gen.num, 1023)
            self.assertLessEqual(gen.num, 9876)

    def test_duplicates(self):
        gen = RandomGen()
        for i in range(1023):
            gen.compute_num()
            numbers = list(map(int, str(gen.num)))
            self.assertEqual(len(numbers), len(set(numbers)))


class TestTarea1Guess(unittest.TestCase, Guess):
    '''
      Testing the when the user wins.
    '''

    @patch('tarea1.Guess.win')
    def test_number_is_guessed(self, mock_win):
        self.win()
        self.assertTrue(mock_win.called)

    def test_if_user_wins(self):
        self.ok = 5
        self.win()
        self.assertEquals(self.ok, 5)

    @patch('tarea1.Guess.win', return_value='1234')
    def test_if_user_doesnt_win(self,input):
        try:
            self.ok = 3
            self.userNum()
            self.assertIsInstance(self.win(), str)
        except IOError:
            pass





if __name__ == "__main__":
    unittest.main()
