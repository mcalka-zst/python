import sys

linia = sys.stdin.readline().rstrip() #rstrip usuwa białe znaki z końca linii
print(linia)
liczby = linia.split() #split zamienia tekst na listę (wg. spacji), 
print(liczby)
liczby2 = [int(x) for x in liczby]
print(liczby2)
