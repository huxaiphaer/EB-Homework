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
		#q = 0
		ok = []
		no = []
		conjuntos = [1234,7890]
		conjuntos2 = [1235, 1236]
		conjuntos21 = [4563,4562]
		#conjuntos22 = [5890,6890]
		conjuntos23 = [5678,5679]		
		conjuntos3 = [8905, 8906]
		conjuntos31 = [7568, 7569]
		#conjuntos32 = [5321, 6321]
		conjuntos33 = [5643,5642]	
		conjuntos4 = [1235,3456,2456]	
		conjuntos41 = [6890, 5678,5679]
		conjuntos5 = [6890,5678,5679]
		conjuntos51 = [1235,5643,5642]

		q = int(input("Su número es el %d?   "% conjuntos[0]))
		q2 = int(input("Su número es el %d?   "% conjuntos[1]))
		## si la suma de ambos grupos da 4 --> 5 y 6 se descartan.		
		if 	q + q2 == 4: no.extend([5,6])
		
		## q + q2 == 3: definir 5 y 6 a partir del grupo con menos positivos(conjuntos[0]).
		if q == 1 and q2 == 2:
			q3 = int(input("Su número es el %d?   "% conjuntos2[0]))
			q4 = int(input("Su número es el %d?   "% conjuntos2[1]))
			# el mayor va a contener al positivo (5 o 6).		
			if q3 > q4: 
				no.append(6)
				ok.append(5)
			else:
				no.append(5)
				ok.append(6)
			## defino positivos del 1 al 4
			# si aparte de 5 o 6 hay otro positivo entre los restantes, 4 es negativo.				
			if q3 + q4 == 3: 
				no.append(4)
				q5 = int(input("Su número es el %d?   "% conjuntos21[0]))
				if q5 == 2: 
					ok.append(3)
					no.extend([1,2])
				elif q5 == 1:
					q6 = int(input("Su número es el %d?   "% conjuntos21[1]))
					if q6 == 2:
						ok.append(2)
						no.extend([1,3])
					else:
						ok.append(1)
						no.extend([2,3])
			# si no hay otro positivo, 4 es positivo, 1 2 y 3 negativos.			
			elif q3 + q4 == 1: 
				ok.append(4)
				no.extend([1,2,3])
			## habiendo definido 5, 6 y los positivos entre 1 y 4 defino positivos entre 7 y 0
			if 5 in ok: conjuntos22 = 5890
			elif 6 in ok: conjuntos22 = 6890
			
			q7 = int(input("Su número es el %d?   "% conjuntos22))
			if q7 == 3: 
				no.append(7)
				q8 = int(input("Su número es el %d?   "% conjuntos23[0]))
				if q8 == 1:
					no.append(8)
					ok.extend([9,0])
				elif q8 == 2:
					ok.append(8)
					q12 = int(input("Su número es el %d?   "% conjuntos23[1]))
					if q9 == 2:
						ok.append(9)
						no.append(0)
			elif q7 == 2: 
				ok. append(7)
				q8 = int(input("Su número es el %d?   "% conjuntos23[0]))
				if q8 == 3:
					ok.append(8)
					no.extend([9,0])
				elif q8 == 2:
					q9 = int(input("Su número es el %d?   "% conjuntos23[1]))
					if q9 == 3:
						ok.append(9)
						no.extend([8,0])
					elif q9 == 2:
						ok.append(0)
						no.extend([8,9])

		## q + q2 == 3: definir 5 y 6 a partir del grupo con menos positivos(conjuntos[1]).
		elif q == 2 and q2 == 1:
			q13 = int(input("Su número es el %d?   "% conjuntos3[0]))
			q14 = int(input("Su número es el %d?   "% conjuntos3[1]))
			# el mayor va a contener al positivo (5 o 6).			
			if q13 > q14: 
				no.append(6)
				ok.append(5)
			else:
				no.append(5)
				ok.append(6)
			## defino positivos del 7 al 0
			# si aparte de 5 o 6 hay otro positivo entre los restantes, 7 es negativo.					
			if q13 + q14 == 3: 
				no.append(7)
				q15 = int(input("Su número es el %d?   "% conjuntos31[0]))
				if q15 == 2: 
					ok.append(8)
					no.extend([9,0])
				elif q15 == 1:
					q16 = int(input("Su número es el %d?   "% conjuntos31[1]))
					if q16 == 2:
						ok.append(9)
						no.extend([8,0])
					else:
						ok.append(0)
						no.extend([8,9])
			# si no hay otro positivo, 7 es positivo.			
			elif q13 + q14 == 1: 
				ok.append(7)
				no.extend([8,9,0])
			## habiendo definido 5, 6 y los positivos entre 7 y 0 defino positivos entre 1 y 4
			if 5 in ok: conjuntos32 = 5321
			elif 6 in ok: conjuntos32 = 6321

			q17 = int(input("Su número es el %d?   "% conjuntos32))
			if q17 == 3: 
				no.append(4)
				q18 = int(input("Su número es el %d?   "% conjuntos33[0]))
				if q18 == 1:
					no.append(3)
					ok.extend([2,1])
				elif q18 == 2:
					ok.append(3)
					q19 = int(input("Su número es el %d?   "% conjuntos33[1]))
					if q19 == 2:
						ok.append(2)
						no.append(1)
			elif q17 == 2: 
				ok. append(4)
				q18 = int(input("Su número es el %d?   "% conjuntos33[0]))
				if q18 == 3:
					ok.append(3)
					no.extend([2,1])
				elif q18 == 2:
					q19 = int(input("Su número es el %d?   "% conjuntos33[1]))
					if q19 == 3:
						ok.append(2)
						no.extend([3,1])
					elif q19 == 2:
						ok.append(1)
						no.extend([3,2])
		
		## q == 2 q2 == 2. 
		elif q == 2 and q2 == 2:
			## defino positivos del 1 al 4.
			q3 = int(input("Su número es el %d?   "% conjuntos4[0]))
			#si en 123 hay 1 positivo, 4 es positivo
			if q3 == 1:
				ok.append(4)
				q4 = int(input("Su número es el %d?   "% conjuntos4[1]))
				if q4 == 2:
					ok.append(3)
					no.extend([1,2])
				elif q4 == 1:
					no.append(3)
					q5 = int(input("Su número es el %d?   "% conjuntos4[2]))
					if q5 == 2:
						ok.append(2)
						no.append(1)
					elif q5 == 1:
						ok.append(1)
						no.append(2)
			#si en 123 hay 2 positivos, 4 es negativo
			elif q3 == 2:
				no.append(4)
				q4 = int(input("Su número es el %d?   "% conjuntos4[1]))
				if q4 == 0:
					ok.extend([1,2])
					no. append(3)
				elif q4 == 1:
					ok.append(3)
					q5 = int(input("Su número es el %d?   "% conjuntos4[2]))
					if q5 == 1:
						ok.append(2)
						no.append(1)
					elif q5 == 0:
						ok.append(1)
						no.append(2)
			## defino positivos del 7 al 0.
			q4 = int(input("Su número es el %d?   "% conjuntos41[0]))
			#si en 890 hay 1 positivo, 7 es positivo
			if q4 == 1:
				ok.append(7)
				q5 = int(input("Su número es el %d?   "% conjuntos41[1]))
				if q5 == 2:
					ok.append(8)
					no.extend([9,0])
				elif q5 == 1:
					no.append(8)
					q6 = int(input("Su número es el %d?   "% conjuntos41[2]))
					if q6 == 2:
						ok.append(9)
						no.append(0)
					elif q6 == 1:
						ok.append(0)
						no.append(9)
			#si en 890 hay 2 positivos, 7 es negativo
			elif q4 == 2:
				no.append(7)
				q5 = int(input("Su número es el %d?   "% conjuntos41[1]))
				if q5 == 0:
					ok.extend([9,0])
					no. append(8)
				elif q5 == 1:
					ok.append(8)
					q6 = int(input("Su número es el %d?   "% conjuntos41


						[2]))
					if q6 == 1:
						ok.append(9)
						no.append(0)
					elif q6 == 0:
						ok.append(0)
						no.append(9)
			
		## q == 3 and q2 == 1.
		elif q == 3 and q2 == 1:
			#defino grupo con 1 positivo
			q3 = int(input("Su número es el %d?   "% conjuntos5[0]))
			if q3 == 0:
				ok.append(7)
				no.extend([8,9,0])
			elif q3 == 1:
				no.append(7)
				q4 = int(input("Su número es el %d?   "% conjuntos5[1]))
				if q4 == 1:
					ok.append(8)
					no.extend([9,0])
				elif q4 == 0:
					no.append(8)
					q5 = int(input("Su número es el %d?   "% conjuntos5[2]))
					if q5 == 1:
						ok.append(9)
						no.append(0)
					elif q5 == 0:
						ok.append(0)
						no.append(9)
			#defino grupo con 3 positivos
			q4 = int(input("Su número es el %d?   "% conjuntos51[0]))
			if q4 == 3:
				no.append(4)
				ok.extend([1,2,3])
			elif q4 == 2:
				ok.append(4)
				q5 = int(input("Su número es el %d?   "% conjuntos51[1]))
				if q5 == 2:
					ok.append(3)
					q6 = int(input("Su número es el %d?   "% conjuntos51[2]))
					if q6 == 2:
						ok.append(2)
						no.append(1)
					elif q6 == 1:
						ok.append(1)
						no.append(2)
				elif q5 == 1:
					no.append(3)
					q6 = int(input("Su número es el %d?   "% conjuntos51[2]))
					if q6 == 2:
						ok.append(2)
						no.append(1)
					elif q6 == 1:
						ok.append(1)
						no.append(2)

		## q == 1 and q2 == 3.
		elif q == 1 and q2 == 3:
			#defino grupo con 1 positivo
			q4 = int(input("Su número es el %d?   "% conjuntos51[0]))
			if q4 == 0:
				ok.append(4)
				no.extend([1,2,3])
			elif q4 == 1:
				no.append(4)
				q5 = int(input("Su número es el %d?   "% conjuntos51[1]))
				if q5 == 1:
					ok.append(3)
					no.extend([1,2])
				elif q5 == 0:
					no.append(3)
					q6 = int(input("Su número es el %d?   "% conjuntos51[2]))
					if q6 == 1:
						ok.append(2)
						no.append(1)
					elif q6 == 0:
						ok.append(1)
						no.append(2)
			#defino grupo con 3 positivos
			q3 = int(input("Su número es el %d?   "% conjuntos5[0]))
			if q3 == 3:
				no.append(7)
				ok.extend([8,9,0])
			elif q3 == 2:
				ok.append(7)
				q5 = int(input("Su número es el %d?   "% conjuntos5[1]))
				if q5 == 2:
					ok.append(8)
					q6 = int(input("Su número es el %d?   "% conjuntos5[2]))
					if q6 == 2:
						ok.append(9)
						no.append(0)
					elif q6 == 1:
						ok.append(0)
						no.append(9)
				elif q5 == 1:
					no.append(8)
					ok.extend([9,0])

		print(ok, no)



def main():
    comenzar = Guess()
    comenzar.wellcome()
    comenzar.find_regulars()

if __name__ == "__main__":
	main()


#__________________________________________________________________
#code holder#

'''
elif 6 in ok:
				q10 = int(input("Su número es el %d?   "% conjuntos22[1]))
				if q10 == 3: 
					no.append(7)
					q11 = int(input("Su número es el %d?   "% conjuntos23[0]))
					if q11 == 1:
						no.append(8)
						ok.extend([9,0])
					elif q11 == 2:
						ok.append(8)
						q12 = int(input("Su número es el %d?   "% conjuntos23[1]))
						if q12 == 2:
							ok.append(9)
							no.append(0)
				elif q10 == 2: 
					ok. append(7)
					q11 = int(input("Su número es el %d?   "% conjuntos23[0]))
					if q11 == 3:
						ok.append(8)
						no.extend([9,0])
					elif q11 == 2:
						q12 = int(input("Su número es el %d?   "% conjuntos23[1]))
						if q12 == 3:
							ok.append(9)
							no.extend([8,0])
						elif q12 == 2:
							ok.append(0)
							no.extend([8,9])

elif 6 in ok:
				q20 = int(input("Su número es el %d?   "% conjuntos32[1]))
				if q20 == 3: 
					no.append(4)
					q18 = int(input("Su número es el %d?   "% conjuntos33[0]))
					if q18 == 1:
						no.append(3)
						ok.extend([2,1])
					elif q18 == 2:
						ok.append(3)
						q19 = int(input("Su número es el %d?   "% conjuntos33[1]))
						if q19 == 2:
							ok.append(2)
							no.append(1)
				elif q20 == 2: 
					ok. append(4)
					q18 = int(input("Su número es el %d?   "% conjuntos33[0]))
					if q18 == 3:
						ok.append(3)
						no.extend([2,1])
					elif q18 == 2:
						q19 = int(input("Su número es el %d?   "% conjuntos33[1]))
						if q19 == 3:
							ok.append(2)
							no.extend([3,1])
						elif q19 == 2:
							ok.append(1)
							no.extend([3,2])

'''							