s="Ala ma hipopotama"
i=int(input("Nr znaku do zamiany: "))
ch=input("Wpisz nowy znak: ")
slist=list(s)
slist[i]=ch
print(slist)
s="".join(slist)
print(s)