from random import randint

class User():

	def __init__(self):
		self.name = input("""Indique su nombre para comenzar:
			
			""")
	"""def name(self):
		nombre = self.user
		print(nombre)"""

	def userNum(self):
		self.user_num = int(input("diga un número de 4 cifras:"))

class Computer(User):
	#def __init__(self):
		#self.user = input("Indique su nombre para comenzar")
	def wellcome(self):
		msg = "Bienvenido %s, en el siguiente juego usted debe adivinar cual es el número de 4 cifras que ha pensado el ordenador." % self.name
		print(msg)

	def num(self):
		random = randint(1023, 9876)
		random = list(map(int, str(random)))
		while random[0] == random[1] or random[0] == random[2] or random[0] == random[3] or random[1] == random[2] or random[1] == random[3] or random[2] == random[3]:
			random = randint(1023, 9876)
			random = list(map(int, str(random)))
		num = ""
		self.num = int(num.join(map(str,random)))
		
class Guess(Computer):
	def guess(self):
		pass



def main():
    comenzar = Computer()
    comenzar.wellcome()
    #comenzar.userNum()
    comenzar.num()
    print(comenzar.num)

if __name__ == "__main__":
	main()

