import os
os.system("cls")

def silnia(n):
    wynik=1
    for i in range (1,n+1):
        wynik*=i
    return wynik


n = int(input("n = "))
k = int(input("k = "))

kombinacje = int(silnia(n)/(silnia(k)*(silnia(n-k))))
print(kombinacje)