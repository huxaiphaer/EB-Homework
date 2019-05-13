from random import randint

class User():

	def __init__(self):
		#self.name = input("Indique su nombre para comenzar:  ")
		self.name = "a"

	'''def userNum(self):
		self.user_num = int(input("diga un número de 4 cifras:"))
		while len(str(self.user_num)) != 4:
			self.user_num = int(input("Número inválido.\nDiga un número de 4 cifras:"))
		for i in range(len(str(self.user_num))):
			for j in range(i+1,len(str(self.user_num))):
				while str(self.user_num)[i] == str(self.user_num)[j]:
					self.user_num = int(input("Número inválido: ninguna cifra debe repetirse.\nDiga un número de 4 cifras:"))'''

class Host(User):

	def wellcome(self):
		msg = "Bienvenido %s, en el siguiente juego usted debe decir un número de 4 cifras (ninguna debe repetirse) y el ordenador adivinará cual es la cifra que eligió.\nIndicar cuantas cifras son correctas(no importa si están en otra posición)." % self.name.upper()
		print(msg)

	'''def num(self):
		random = randint(1023, 9876)
		random = list(map(int, str(random)))
		while random[0] == random[1] or random[0] == random[2] or random[0] == random[3] or random[1] == random[2] or random[1] == random[3] or random[2] == random[3]:
			random = randint(1023, 9876)
			random = list(map(int, str(random)))
		num = ""
		self.num = int(num.join(map(str,random)))'''

class Guess(Host):

	def find_regulars(self):
		si = 0
		ok = []
		no = []
		conjuntos = [1234,7890]
		conjuntos2 = [1235, 1236]
		conjuntos21 = [4563,4562]
		conjuntos22 = [5890,6890]
		conjuntos23 = [5678,5679]		
		conjuntos3 = [8905, 8906]

		si = int(input("Su número es el %d?   "% conjuntos[0]))
		si2 = int(input("Su número es el %d?   "% conjuntos[1]))
		# si la suma de ambos grupos da 4 -> 5 y 6 se descartan.		
		if 	si + si2 == 4: no.extend([5,6])
		# si da 3 procedo a descartar 5 o 6 a partir del grupo con menos positivos (grupo1).
		if si == 1 and si2 == 2:
			si3 = int(input("Su número es el %d?   "% conjuntos2[0]))
			si4 = int(input("Su número es el %d?   "% conjuntos2[1]))
			# el mayor va a contener al positivo (5 o 6).		
			if si3 > si4: 
				no.append(6)
				ok.append(5)
			else:
				no.append(5)
				ok.append(6)
			# si aparte de 5 o 6 hay otro positivo entre los restantes, 4 es negativo.				
			if si3 + si4 == 3: 
				no.append(4)
				si5 = int(input("Su número es el %d?   "% conjuntos21[0]))
				if si5 == 2: 
					ok.append(3)
					no.extend([1,2])
				elif si5 == 1:
					si6 = int(input("Su número es el %d?   "% conjuntos21[1]))
					if si6 == 2:
						ok.append(2)
						no.extend([1,3])
					else:
						ok.append(1)
						no.extend([2,3])
			# si no hay otro positivo, 4 es positivo, 1 2 y 3 negativos.			
			elif si3 + si4 == 1: 
				ok.append(4)
				no.extend([1,2,3])
			# habiendo definido 5, 6 y los positivos entre 1 y 4 paso definir los positivos entre 7 y 0
			if 5 in ok:
				si7 = int(input("Su número es el %d?   "% conjuntos22[0]))
				if si7 == 3: 
					no.append(7)
					si8 = int(input("Su número es el %d?   "% conjuntos23[0]))
					if si8 == 1:
						no.append(8)
						ok.extend([9,0])
					elif si8 == 2:
						ok.append(8)
						si12 = int(input("Su número es el %d?   "% conjuntos23[1]))
						if si9 == 2:
							ok.append(9)
							no.append(0)
				elif si7 == 2: 
					ok. append(7)
					si8 = int(input("Su número es el %d?   "% conjuntos23[0]))
					if si8 == 3:
						ok.append(8)
						no.extend([9,0])
					elif si8 == 2:
						si9 = int(input("Su número es el %d?   "% conjuntos23[1]))
						if si9 == 3:
							ok.append(9)
							no.extend([8,0])
						elif si9 == 2:
							ok.append(0)
							no.extend([8,9])

			elif 6 in ok:
				si10 = int(input("Su número es el %d?   "% conjuntos22[1]))
				if si10 == 3: 
					no.append(7)
					si11 = int(input("Su número es el %d?   "% conjuntos23[0]))
					if si11 == 1:
						no.append(8)
						ok.extend([9,0])
					elif si11 == 2:
						ok.append(8)
						si12 = int(input("Su número es el %d?   "% conjuntos23[1]))
						if si12 == 2:
							ok.append(9)
							no.append(0)
				elif si10 == 2: 
					ok. append(7)
					si11 = int(input("Su número es el %d?   "% conjuntos23[0]))
					if si11 == 3:
						ok.append(8)
						no.extend([9,0])
					elif si11 == 2:
						si12 = int(input("Su número es el %d?   "% conjuntos23[1]))
						if si12 == 3:
							ok.append(9)
							no.extend([8,0])
						elif si12 == 2:
							ok.append(0)
							no.extend([8,9])


		# si da 3 procedo a descartar 5 o 6 a partir del grupo con menos positivos(grupo2).
		'''elif si == 3 and si2 == 1:
			si7 = int(input("Su número es el %d?   "% conjuntos3[0]))
			si8 = int(input("Su número es el %d?   "% conjuntos3[1]))
			# el mayor va a contener al positivo (5 o 6).			
			if si7 > si8: 
				no.append(6)
				ok.append(5)
			else:
				no.append(5)
				ok.append(6)
			# si aparte de 5 o 6 hay otro positivo entre los restantes, 7 es negativo.					
			if si7 == 2 and si8 == 1: no.append(7)
			# si no hay otro positivo, 7 es positivo.			
			if si3 == 1 and si4 == 0: ok.append(7)'''


		print(ok, no)



def main():
    comenzar = Guess()
    comenzar.wellcome()
    #comenzar.num()
    #print(comenzar.num)
    #comenzar.userNum()
    comenzar.find_regulars()

if __name__ == "__main__":
	main()

