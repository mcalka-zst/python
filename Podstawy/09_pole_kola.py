import math
import os

os.system("cls")
r= float(input("Podaj promień r="))
if r>0:
    pole=math.pi*r*r
    print(f"Pole = {pole}")
else:
    print("Wpisz r>0")
