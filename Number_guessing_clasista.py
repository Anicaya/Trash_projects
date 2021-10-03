from numpy import random
from numpy.random.mtrand import rand

class Num_oculto():
    def __init__(self) -> None:
        self.random_num()

    def random_num(self):
        self.rnum = random.randint(100)

    def number_hint_guess(self):
        num = -1
        while num != self.rnum:
            
            self.guess_rnum = random.randint(4)
            if self.guess_rnum == 0: 
                if self.rnum > num: print("El número es mayor que el que has puesto")
                else: print("El número es menor que el que has puesto")
            if self.guess_rnum == 1:
                if self.rnum %2 == 0: print("El número es par")
                else: print("El número es impar")
            if self.guess_rnum == 2:
                if self.rnum > 50: print("El número es mayor de 50")
                else: print("El número menor de 50")
            if self.guess_rnum == 3:
                if self.rnum % num == 0: print("El número es divisible entre tu numero")
                else: print("El número no es divisible entre tu número")

            num = int(input("Intenta adivinar el número: "))

        print(f"Felicidades, lo has adivinado, el numero era {self.rnum}")

rip = Num_oculto()
rip.number_hint_guess()



    