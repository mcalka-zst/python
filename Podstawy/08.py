import os
os.system("cls")

staz = int(input("Podaj staż pracy = "))

if staz<=0:
    zarobki = 0
elif staz<=5:
    zarobki = 1500 + 120*staz
else:
    zarobki = 2300 + 100*staz
print("Zarabiasz %.2fzł" % zarobki)