import os
os.system("cls")
#-------------------------
class Dog:
    def __init__(self):
        print("Utworzono psa - działa konstruktor klasy Dog")

    def read(self):
        self.imie = input("Podaj imie psa: ")

    def giveVoice(self):
        print(f"{self.imie} mówi hau hau")

#-------------------------
class BadDog(Dog):
    def __init__(self):
        super().__init__()
        print("Utworzono złego psa - działa konstruktor klasy BadDog")

    def giveVoice(self):
        super().giveVoice()
        print(f"{self.imie} mówi wrrrrr! Dajcie mi listonosza!!!")
#-------------------------

p1 = Dog()
p1.read()
p1.giveVoice()
print()
p2 = BadDog()
p2.read()
p2.giveVoice()

