from collections import namedtuple
import os
import math
from unicodedata import name

os.system("cls")

#------------------------------------------------------------------------------
class triangle:
    def __init__(self):
        pass

    def read(self):
        ok = False
        while(not ok):
            self.__a = float(input("a = "))
            self.__b = float(input("b = "))
            self.__c = float(input("c = "))
            if(self.__a <= 0 or self.__b <= 0 or self.__c <= 0 or self.__a+self.__b >= self.__c or self.__a+self.__c >= self.__b or self.__b+self.__c >= self.__a):
                ok = True
            else:
                print("Podałeś błędne dane!")


    def field(self):
        p=(self.__a + self.__b + self.__c)/2
        return math.sqrt(p*(p-self.__a)*(p-self.__b)*(p-self.__c))
#------------------------------------------------------------------------------  
n = int(input("Wpisz z ilu trójkatów składa się działka: "))
sum = 0
triangles = [triangle() for i in range(n)] #tablice obiektów
for i in range(n):
    print("Trójkąt nr "+str(i+1))
    triangles[i].read()
    sum+=triangles[i].field()
print("Pole działki: "+str(sum))