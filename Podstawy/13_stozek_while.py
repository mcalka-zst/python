import math
import os

os.system("cls")
r, h = 0, 0
while r <= 0 or h <= 0:
    r = float(input("Podaj promień r = "))
    h = float(input("Podaj wysokość h = "))
    if r <= 0:
        print("Gdzie widziałeś koło z ujemnym promieniem?!")
    if h <= 0:
        print("Gdzie widziałeś ujemną wysokość?!")
pole = math.pi*r*r
print(f"Pole = {pole}")
