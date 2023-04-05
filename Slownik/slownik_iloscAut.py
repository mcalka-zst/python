auta={}
auta["opel"]=5
auta["mercedes"]=2
auta["fiat"]=3
auta["skoda"]=12
auta["ford"]=13

for marka in auta:
    print("Mamy %d samochodów marki %s" % (auta[marka],marka))


print("\nUsuwany dwie marki na dwa sposoby")
del auta["skoda"]
auta.pop("ford")
for marka in auta:
    print("Mamy %d samochodów marki %s" % (auta[marka],marka))
