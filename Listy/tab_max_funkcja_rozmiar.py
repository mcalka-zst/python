def wczytaj(t):
    n=int(input("Podaj rozmiar listy: "))
    for i in range (n):
          temp=int(input("Podaj element: "))
          t.append(temp)
          
def max(t):
    max=tab[0]
    for i in range(1,len(tab)):
        if(max<tab[i]):
            max=tab[i]
    return max
#---------------------------------
tab=[]
wczytaj(tab)
print("Element maksymalny tablicy %s to %d" %(tab,max(tab)))
