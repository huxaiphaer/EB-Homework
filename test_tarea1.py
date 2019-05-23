import unittest
import unittest.mock
from unittest.mock import patch, call
from tarea1 import User, Guess
import io
#import StringIO
import sys



class TestTarea1User(unittest.TestCase, User):

	@patch('builtins.input', side_effect=["36","1","12345", "1234"])
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

	@patch('builtins.input', side_effect=["1224","1090","1255", "1234"])
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

		
if __name__ == "__main__":
    unittest.main()

#_____________________________________

# Code container:

# @patch('builtins.print', side_effect=['¡¡FELICITACIONES ADIVINÓ EL NÚMERO!!'])
# 	def test_win(self, input_mock):
# 		self.ok = 4
# 		expected = [ 
# 		call(), 
# 		# call('Indique un número de 4 cifras:'),
# 		# call('Indique un número de 4 cifras:'),
# 		# call('Indique un número de 4 cifras:'),
# 		#call(None)
# 		#call(print('¡¡FELICITACIONES ADIVINÓ EL NÚMERO!!'))
# 		]
# 		self.win()
# 		self.assertEqual(input_mock.mock_calls, expected)

# @patch('builtins.print')
# def test_print(self, mocked_print):
# 	print('foo')
# 	print()

# 	assert mocked_print.mock_calls == [call('foo'), call()]

# @patch('sys.stdout', new_callable=io.StringIO)
# def assert_stdout(self, mock_stdout):
# 	#n = "'¡¡FELICITACIONES ADIVINÓ EL NÚMERO!!'"
# 	self.ok = 4
# 	#self.foo(n)
# 	self.win()
# 	assert mock_stdout.getvalue() == '¡¡FELICITACIONES ADIVINÓ EL NÚMERO!!'
# 	self.assertEqual(mock_stdout.getvalue(), '¡¡FELICITACIONES ADIVINÓ EL NÚMERO!!')
	#self.assertEqual(mock_stdout.getvalue(), expected_output)
