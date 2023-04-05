class ulamek:
    licznik, mianownik = 1, 1

    def __init__(self, l, m):  # prawie jak konstruktor
        self.licznik = l
        self.mianownik = m
        nwd = NWD(l, m)
        if(nwd != 1):
            self.licznik /= nwd
            self.mianownik /= nwd
            #print("Ułamek został skrócony: %d/%d" % (self.licznik,self.mianownik))
# -----------------------------------------------------------------------------------


def iloczyn(u, v):
    print("Mnożymy")
    l = u.licznik*v.licznik
    m = u.mianownik*v.mianownik
    wynik = ulamek(l, m)
    return wynik
# -----------------------------------------------------------------------------------


def suma(u, v):
    print("Dodajemy")
    wspolny = NWW(u.mianownik, v.mianownik)
    l = u.licznik*wspolny/v.mianownik+v.licznik*wspolny/u.mianownik
    m = wspolny
    wynik = ulamek(l, m)
    return wynik
# -----------------------------------------------------------------------------------


def wyswietl(z):
    print("%d/%d" % (z.licznik, z.mianownik))
# -----------------------------------------------------------------------------------


def NWD(a, b):
    if(b == 0):
        return a
    return NWD(b, a % b)
# -----------------------------------------------------------------------------------


def NWW(a, b):
    return a*b/NWD(a, b)


# -----------------------------------------------------------------------------------
k = int(input("Podaj licznik: "))
m = int(input("Podaj mianownik: "))
u = ulamek(k, m)
l = int(input("Podaj licznik: "))
n = int(input("Podaj mianownik: "))
v = ulamek(l, n)

z = iloczyn(u, v)
wyswietl(z)

s = suma(u, v)
wyswietl(s)
