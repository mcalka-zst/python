from pakiety import wektory
u=wektory.wektor()
v=wektory.wektor()
print("Wektor u: ")
u.wczytaj()
print("Wektor v: ")
v.wczytaj()
z=wektory.wektor()
z=wektory.suma(u,v)
il=wektory.iloczyn(u,v)
print("\n|u| = %s" % u.dlugosc())
print("|v| = %s" % v.dlugosc())
print("\nSuma")
u.wyswietl()
print(" + ",end='') #dzięki ,end='' nie przechodzimy do nowej linii
u.wyswietl()
print(" = ",end='')
z.wyswietl()
print("\n\nIloczyn skalarny")
u.wyswietl()
print(" o ",end='') 
u.wyswietl()
print(" = %s" % il,end='')


