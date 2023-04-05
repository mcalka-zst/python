import os
os.system("cls")
# ------------------------------


class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def write(self):
        print(f"{self.name} ma {self.age} lat i waży {self.weight} kg")
# ------------------------------


class Cat(Animal):
    def write(self):
        super().write()
        print("I na dodatek jest Catem\n")

# ------------------------------


class Dog(Animal):
    def write(self):
        super().write()
        print("I na dodatek jest psem\n")


class Hen(Animal):
    def __init__(self, name, age, weight, color):
        super().__init__(name, age, weight)
        self.color = color

    def write(self):
        super().write()
        print(f"I na dodatek jest kurą, a jej kolor - {self.color}\n")


# ------------------------------
Zwierz = Animal("Nie wiadomo jaki Zwierz", 15, 57)
Mruczek = Cat("Mruczek", 10, 5)
Azor = Dog("Azor", 9, 20)
Kokoszka = Hen("Kokoszka", 2, 3, "czarny")

Zwierz.write()
Mruczek.write()
Azor.write()
Kokoszka.write()
