import math
class wektor:
    x,y=0,0
    def dlugosc(self): #self odpowiednik this z C++,  nie jest zastrzeżone
        return math.sqrt(self.x*self.x+self.y*self.y)
def suma(u,v):
    z=wektor()
    z.x=u.x+v.x
    z.y=u.y+v.y
    return z
def iloczyn(u,v):
    return u.x*v.x+u.y*v.y
    
u=wektor()
u.x=float(input("Podaj współrzędną x wektora u: "))
u.y=float(input("Podaj współrzędną y wektora u: "))
v=wektor()
v.x=float(input("Podaj współrzędną x wektora v: "))
v.y=float(input("Podaj współrzędną y wektora v: "))
print("Długość wektora u=[%s, %s] wynosi %s" % (u.x, u.y, u.dlugosc()))
print("Długość wektora v=[%s, %s] wynosi %s" % (v.x, v.y, v.dlugosc()))
s=suma(u,v)
print("u + v= [%s, %s]" % (s.x, s.y))

print("u o v= %s" % iloczyn(u,v))
