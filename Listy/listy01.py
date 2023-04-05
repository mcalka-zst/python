tab1=[]
tab1.append(3)
tab1.append(2.4)
tab1.append(30.9876)
tab1.append(-7)
print('Pierwsza tablica:')
for x in tab1:
    print(x)
print('Pierwsza tablica inaczej: %s' % tab1)
#--------------------
print('Druga tablica:')
tab2=[2,4,5.6,12]
for x in tab2:
    print(x)
#--------------------
print('Trzecia tablica:')
tab3=tab1+tab2
for x in tab3:
    print(x)
print("Tablica: %s" % tab3)
#--------------------
tab4 = [9]*26
print("Czwarta tablica: ",end= " ")
print(tab4)