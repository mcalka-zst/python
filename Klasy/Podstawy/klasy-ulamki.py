class ulamek:
    licznik, mianownik = 1, 1

    def skroc(self):
        nwd = NWD(self.licznik, self.mianownik)
        if(nwd != 1):
            self.licznik /= nwd
            self.mianownik /= nwd
            print("Ułamek został skrócony: %d/%d" %
                  (self.licznik, self.mianownik))
        return self
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
u = ulamek()
u.licznik = int(input("Podaj licznik: "))
u.mianownik = int(input("Podaj mianownik: "))
u = u.skroc()
v = ulamek()
v.licznik = int(input("Podaj licznik: "))
v.mianownik = int(input("Podaj mianownik: "))
v = v.skroc()
m = ulamek()
z = iloczyn(u, v)
s = ulamek()
s = suma(u, v)
wyswietl(z)
wyswietl(s)
