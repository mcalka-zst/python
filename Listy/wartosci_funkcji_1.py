import os
os.system("cls")
a = 1
b = -6
c = 8
y = [a*x**2+b*x+c for x in range(-7, 14, 1)] # 1 można pominąć
print(y)
print()
for i in range(len(y)):
    print("f(%d)=%d" % (i-7, y[i]))
