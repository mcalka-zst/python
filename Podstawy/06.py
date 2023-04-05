import os
os.system("cls")

a = int(input("Podaj bok a = "))

if a > 0: 
    result = a*a #a**2
    print("Pole  = "+str(result))
else:
    print("Podaj dodatnią!!!")