import pakiety.zespolone
z1=pakiety.zespolone.zespolona()
z2=pakiety.zespolone.zespolona()
print("Liczba z1: ")
z1.wczytaj()
print("Liczba z2: ")
z2.wczytaj()
z=pakiety.zespolone.zespolona()

z=pakiety.zespolone.suma(z1,z2)
il=pakiety.zespolone.iloczyn(z1,z2)
print("\n|z1| = %s" % z1.modul())
print("|z2| = %s" % z2.modul())
print("\nSuma")
z1.wyswietl()
#dzięki ,end='' nie przechodzimy do nowej linii, domyślnie end='\n'
print(" + ",end='') 
z2.wyswietl()
print(" = ",end='')
z.wyswietl()
print("\n\nIloczyn ")
z1.wyswietl()
print(" * ",end='')
z2.wyswietl()
print(" = ",end='')
z.wyswietl()

