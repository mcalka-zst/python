def max(t):
    max=tab[0]
    for i in range(1,len(tab)):
        if(max<tab[i]):
            max=tab[i]
    return max
#---------------------------------
tab=[2,3,6,-1,5,8,4]
print("Element maksymalny tablicy %s to %d" %(tab,max(tab)))
