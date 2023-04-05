import operator
import os

os.system("cls")
#https://developers.google.com/edu/python/sorting

text = "goryl krokodyl lew zebra hiena"
tab=text.split()
print(tab)
print()

tab.sort()
print(tab)

tab=text.split()
tab.sort(reverse=True)
print(tab)

tab=text.split()
tab.sort(key=len)
print(tab)

tab=text.split()
tab.sort(key=len, reverse=True)
print(tab)