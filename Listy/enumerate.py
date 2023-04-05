import os
os.system("cls")
names = ["Jasio", "Stasio","Franio","Pawełek","Pioruś","Henio"]
for name in names:
     print(name, end=" ")
print()
print()
for index, name in enumerate(names):
    print(index,"-", name)