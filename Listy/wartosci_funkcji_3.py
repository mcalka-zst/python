import os
os.system("cls")
a = 1
b = -6
c = 8
x = range(-7, 14)
y = [a*i**2+b*i+c for i in x]
print(y)
print()
for i in range(len(y)):
    print("f(%d)=%d" % (x[i], y[i]))
