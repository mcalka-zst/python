import pakiety.wektory
u = pakiety.wektory.wektor()
v = pakiety.wektory.wektor()
print("Wektor u: ")
u.wczytaj()
print("Wektor v: ")
v.wczytaj()
z = pakiety.wektory.wektor()
z = pakiety.wektory.suma(u, v)
il = pakiety.wektory.iloczyn(u, v)
print("\n|u| = %s" % u.dlugosc())
print("|v| = %s" % v.dlugosc())
print("\nSuma")
u.wyswietl()
# dzięki ,end='' nie przechodzimy do nowej linii, domyślnie end='\n'
print(" + ", end='')
v.wyswietl()
print(" = ", end='')
z.wyswietl()
print("\n\nIloczyn skalarny")
u.wyswietl()
print(" o ", end='')
v.wyswietl()
print(" = %s" % il, end='')
