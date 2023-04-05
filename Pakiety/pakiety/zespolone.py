import math
class zespolona:
    re,im=0,0
    def wczytaj(self):
        self.re=float(input("Podaj część rzeczywistą liczby: "))
        self.im=float(input("Podaj część urojoną liczby: "))
    def wyswietl(self):
        print("(%s + %si)" % (self.re,self.im), end='') #dzięki ,end='' nie przechodzimy do nowej linii
    def modul(self):
        return math.sqrt(self.re*self.re+self.im*self.im)
def suma(z1,z2):
    z=zespolona()
    z.re=z1.re+z2.re
    z.im=z1.im+z2.im
    return z
def iloczyn(z1,z2):
    z=zespolona()
    z.re=z1.re*z2.re-z1.im*z2.im
    z.im=z1.im*z2.re+z1.re*z2.im
    return z
    
