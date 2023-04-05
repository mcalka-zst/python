import os
os.system("cls")

a = int(input("Podaj podstawę a = "))
b = int(input("Podaj podstawę b = "))
h = int(input("Podaj wysokość h = "))

if a > 0 and b>0 and h>0:
    result = 0.5*(a+b)*h
    print("Pole  = "+str(result))
else:
    print("Podaj dodatnie liczby!!!")
