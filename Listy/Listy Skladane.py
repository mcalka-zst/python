import os
os.system("cls")
#tworzenie jednej tablicy na podstawie innej
tekst="Ala ma hipopotama i żyrafę"
slowa=tekst.split() #tablica słów
print("Mamy tekst: %s \n" % tekst)
for slowo in slowa:
    print("%s ma %d znaków" %(slowo, len(slowo)))
#---------------------------------------
print("\n\n" )
dlugosci = [len(slowo) for slowo in slowa]
print(slowa)
print(dlugosci)
#---------------------------------------
print("\n\n")
print("Tablica liczb rzeczywistych")
tab1=[2.3, 34.6, -87.7, 23.87, 4.6]
tab2=[int(liczba) for liczba in tab1 if liczba>=0]
print(tab1)
print("Tablica liczb naturalnych utworzona na podstawie tab1")
print(tab2)
