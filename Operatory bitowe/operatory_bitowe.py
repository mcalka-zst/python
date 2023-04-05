# DZIAŁAJĄ NA LICZBACH CAŁKOWITYCH
x = 13  # x=1101
y = 11  # x=1011
z = 200  # z=1100 1000
koniunkcja = x & y  # 1101 & 1011 = 1001 = 9 - koniunkcja bitowa
alternatywa = x | y  # 1101 & 1011 = 1111 = 15 - alternatywa bitowa
roznica = x ^ y  # 1101 & 1011 = 0110 = 6 -  bitowa różnica symetryczna
print("%d & %d = %d" % (x, y, koniunkcja))
print("%d | %d = %d" % (x, y, alternatywa))
print("%d ^ %d = %d" % (x, y, roznica))

razy2 = x << 1  # 1101 << 1 = 110 010 = 16 + 8 + 2= 26 - przesunięcie o jeden bit, czyli mnożenie przez 2
razy4 = x << 2  # 1101 << 2 = 110 0100 = 32 + 16 + 4= 52 - przesunięcie o dwa bity, czyli mnożenie przez 4
# 1101 << 10 = 110 0100 0000 0000 =  13312 - przesunięcie o 10 bitów, czyli mnożenie przez 1024
razy1024 = x << 10
print("%d * 2 = %d" % (x, razy2))
print("%d * 4 = %d" % (x, razy4))
print("%d * 1024 = %d" % (x, razy1024))

przez2 = z >> 1  # 11001000‬ >> 1 = ‭1100100 =100
przez4 = z >> 2  # 11001000‬ >> 2 = ‭110010 =50
print("%d / 2 = %d" % (z, przez2))
print("%d / 4 = %d" % (z, przez4))

# Not(13) = ~0000 1101 = 1111 0010 (u2) = -14 ( uzupełnienie bitowe np. na 8 bitach)
uzupelnienie = ~x
print("%d = %d" % (x, uzupelnienie))
