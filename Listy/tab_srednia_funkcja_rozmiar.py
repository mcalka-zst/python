def wczytaj(t):
    n=int(input("Podaj rozmiar tablicy: "))
    for i in range (n):
          temp=int(input("Podaj element: "))
          t.append(temp)
          
def srednia(t):
    suma=0
    n=len(tab)
    for i in range(1,n):
        suma+=tab[i]
    return suma/n
#---------------------------------
tab=[]
wczytaj(tab)
print("Srednia elementów tablicy %s to %f" %(tab,srednia(tab)))
print("Srednia elementów tablicy %s to %s" %(tab,srednia(tab)))
