class ulamek:
     def __init__(self, l, m): #prawie jak konstruktor
          self.licznik=l
          self.mianownik=m
          nwd=NWD(l,m)
          if(nwd!=1):
               self.licznik/=nwd
               self.mianownik/=nwd
               print("Ułamek został skrócony: %d/%d" % (self.licznik,self.mianownik))
#-----------------------------------------------------------------------------------   
def iloczyn(u,v):
    wynik=ulamek(1,1)
    wynik.licznik = u.licznik*v.licznik
    wynik.mianownik = u.mianownik*v.mianownik
    return wynik
#-----------------------------------------------------------------------------------   
def suma(u,v):
    wynik=ulamek(1,1)
    wspolny=NWW(u.mianownik,v.mianownik)
    wynik.licznik=u.licznik*wspolny/v.mianownik+v.licznik*wspolny/u.mianownik
    wynik.mianownik=wspolny
    return wynik
#-----------------------------------------------------------------------------------   
def wyswietl(z):
    print("%d/%d" % (z.licznik,z.mianownik), end=" ")
#-----------------------------------------------------------------------------------   
def NWD(a,b):
    if(b==0):
        return a
    return NWD(b,a%b)
#-----------------------------------------------------------------------------------   
def NWW(a,b):
    return a*b/NWD(a,b)
#-----------------------------------------------------------------------------------   
k=int(input("Podaj licznik: "))
m=int(input("Podaj mianownik: "))
u=ulamek(k,m)
l=int(input("Podaj licznik: "))
n=int(input("Podaj mianownik: "))
v=ulamek(l,n)
z=iloczyn(u,v)
s=suma(u,v)
wyswietl(u)
print(" * ",end=" ")
wyswietl(v)
print(" = ",end=" ")
wyswietl(z)
print()
wyswietl(u)
print(" + ",end=" ")
wyswietl(v)
print(" = ",end=" ")
wyswietl(s)
