import os
os.system("cls")

s = "Ala lubi bigos i bigos lubli Alę, również Ola lubi bigos i bigos lubli Olę!"
s1 = s.replace("bigos", "schab")
s2 = s.replace("bigos", "schab", 1)#zmieni jedno wystąpienie
s3= s.replace("bigos", "schab", 2) #zmieni 2 wystąpienia

print(s)
print(s1)
print(s2)
print(s3)
