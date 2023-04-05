import os
os.system("cls")

lista = [2, 3, 6, -3, 4, -6]
#--------------------------------------------
print(lista[0], end=" ")
print(lista[1], end=" ")
print(lista[2], end=" ")
print(lista[3], end=" ")
print(lista[4], end=" ")
print(lista[5], end=" ")
# print(lista[6], end=" ") # błąd - przekroczony zakres
lista.append(-23)
print(lista[6], end=" ")
print()
#--------------------------------------------
for i in range(len(lista)):
    print(lista[i], end=" ")
print()
#--------------------------------------------
for element in lista:
    print(element, end=" ")