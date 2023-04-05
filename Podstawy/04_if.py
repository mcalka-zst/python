import os
os.system("cls")

x = int(input("x = "))
y = int(input("y = "))
if y == 0:
    print("Nie wolno dzielic przez 0!!!")
else:
    result = x/y
    print(f"{x} / {y} = {result}")
