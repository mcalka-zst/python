class ulamek:
    def __init__(self):  # prawie jak konstruktor
        pass

    def skroc(self):
        nwd = NWD(self.licznik, self.mianownik)
        if(nwd != 1):
            self.licznik /= nwd
            self.mianownik /= nwd
            print("Ułamek został skrócony: %d/%d" %
                  (self.licznik, self.mianownik))
        return self

    def wczytaj(self):
        self.licznik = int(input("Podaj licznik: "))
        self.mianownik = int(input("Podaj mianownik: "))
        self.skroc()

    def wyswietl(self):
        print("%d/%d" % (self.licznik, self.mianownik), end=" ")
# -----------------------------------------------------------------------------------


def iloczyn(u, v):
    wynik = ulamek()
    wynik.licznik = u.licznik*v.licznik
    wynik.mianownik = u.mianownik*v.mianownik
    return wynik
# -----------------------------------------------------------------------------------


def suma(u, v):
    wynik = ulamek()
    wspolny = NWW(u.mianownik, v.mianownik)
    wynik.licznik = u.licznik*wspolny/v.mianownik+v.licznik*wspolny/u.mianownik
    wynik.mianownik = wspolny
    return wynik
# -----------------------------------------------------------------------------------


def NWD(a, b):
    if(b == 0):
        return a
    return NWD(b, a % b)
# -----------------------------------------------------------------------------------


def NWW(a, b):
    return a*b/NWD(a, b)


# -----------------------------------------------------------------------------------
u = ulamek()
u.wczytaj()
v = ulamek()
v.wczytaj()
z = iloczyn(u, v)
s = suma(u, v)
u.wyswietl()
print(" * ", end=" ")
v.wyswietl()
print(" = ", end=" ")
z.wyswietl()
print()
u.wyswietl()
print(" + ", end=" ")
v.wyswietl()
print(" = ", end=" ")
s.wyswietl()
