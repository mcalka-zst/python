import os
os.system("cls")
x = 3.4445565645634234342332423423
y = 4.32323232323234234234324234234234
z = x+y
# domyślnie 16 miejsc po przecinku (bo double)
print(str(x)+" + "+str(y)+" = "+str(z))
# tym sposobem 6 miejsc po przecinku (bo float)
print("%f + %f= %f" % (x, y, z))
# z round i tak wyświetli  się 6 miejsc po przecinku (2 + zera do 6)
print("%f + %f= %f" % (round(x, 4), round(y, 4), round(z, 2)))

# z round i konwersją na string bedzie dobrze ale mało wygodnie przy pisaniu
print(str(round(x, 4))+" + "+str(round(y, 4))+" = "+str(round(z, 2)))

# stary sposób (ale wygodny)
print("%.4f + %.3f= %.2f" % (x, y, z))
# nowy sposób od Pythona 3
print("{:.4f} + {:.3f} = {:.2f}".format(x, y, z))
#f-string formatting
print(f"{x} + {y} = {z}")
