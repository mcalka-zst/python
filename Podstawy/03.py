import os
os.system("cls")

zl = float(input("Podaj kwotę w zł: "))
dolar = zl/4.31
euro =zl/4.5
print(f"{zl}zł to {dolar}$")
print("%.2f zł to %.2f $" % (zl, dolar))
print("%d zł to %d $" % (zl, dolar))
# %d -liczba całkowita
# %.2f liczba zmiennoprzecinkowa - 2 miejsca po przecinku 