from random import randint


def number():
    """
    Genera un número aleatorio de 4 cifras no repetidas que el usuario deberá adivinar.
    """
    conjuntos = [1234, 7890]
    q = int(input("Su número es el %d?\nCifras OK:   " % conjuntos[0])) + int(input("Cifras REGULAR: "))
    q2 = int(input("Su número es el %d?\nCifras OK:   " % conjuntos[1])) + int(input("Cifras REGULAR: "))

    # return num

if __name__ == "__main__":
   number()
