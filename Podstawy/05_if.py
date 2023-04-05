import os
os.system("cls")

x = int(input("x = "))
y = int(input("y = "))
if y != 0: # != różne
    result = x/y
    print(f"{x} / {y} = {result}")
else:
    print("Nie wolno dzielić przez 0!!!")