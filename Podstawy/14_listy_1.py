import os
os.system("cls")

lista = [] #pusta lista
lista.append(2) # dodawanie elementu do listy
lista.append(123)
lista.append(23)
print(lista)
print(f"Lista ma {len(lista)} elementy")
lista.append(-13)
lista.append(233)
print(lista)
print(f"Lista ma {len(lista)} elementy")
lista.pop() # usuwanie ostaniego elementu z listy
print(lista)
print(f"Lista ma {len(lista)} elementy")