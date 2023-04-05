import math
class wektor:
    x,y=0,0
    def wczytaj(self):
        self.x=float(input("Podaj współrzędną x wektora: "))
        self.y=float(input("Podaj współrzędną y wektora: "))
    def wyswietl(self):
        print("[%s, %s]" % (self.x,self.y), end='') #dzięki ,end='' nie przechodzimy do nowej linii
    def dlugosc(self):
        return math.sqrt(self.x*self.x+self.y*self.y)
def suma(u,v):
    z=wektor()
    z.x=u.x+v.x
    z.y=u.y+v.y
    return z
def iloczyn(u,v):
    return u.x*v.x+u.y*v.y
    
