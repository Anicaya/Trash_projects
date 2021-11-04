from numpy import random

class Cow_Bull:
    def __init__(self) -> None:
        self.random_num = [int(x) for x in str(1000 + (random.randint(8999)))]

    def find_num(self):
        cows, bulls = 0,0

        while cows != 4:
            cows, bulls = 0,0
            num = int(input("Número que crees que es: "))
            list_num1 = [int(x) for x in str(num)]

            for i in range(len(list_num1)):
                if list_num1[i] == self.random_num[i]:
                    cows += 1
                if list_num1[i] in self.random_num:
                    bulls += 1

            print(f"Cows: {cows}, Bulls: {bulls}")
        
        

game = Cow_Bull()
game.find_num()
