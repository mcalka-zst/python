import os
os.system("cls")
znak = 'r'
zmnak2 = "t"
nr = ord(znak)
z = chr(nr)
print(z+" ma kod "+str(nr))
tekst = "aa"
tekst += z
print(tekst)
tekst = z+tekst
print(tekst)
tekst += chr(100)
print(tekst)

