import os
os.system("cls")
# ------------------------------


class Zwierze:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def write(self):
        print(f"{self.name} ma {self.age} lat i waży {self.weight} kg")
# ------------------------------


class Kot(Zwierze):
    pass  # operacja pusta - nic się nie dzieje
# ------------------------------


class Pies(Zwierze):
    pass

# ------------------------------
Zwierz = Zwierze("Nie wiadomo jaki Zwierz", 15, 57)
Mruczek = Kot("Mruczek", 10, 5)
Azor = Pies("Azor", 9, 20)

Zwierz.write()
Mruczek.write()
Azor.write()
