import math
import os

os.system("cls")
r=0
while r<=0:
    r = float(input("Podaj promień r = "))
    if r<=0:
        print("Gdzie widziałeś koło z ujemnym promieniem?!")
pole = math.pi*r*r
print(f"Pole = {pole}")

