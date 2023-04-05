auta={
    "opel":5,
    "mercedes":2,
    "fiat":3,
    "skoda":12,
    "ford":13,
}
for marka in auta:
    print("Mamy %d samochodów marki %s" % (auta[marka],marka))
    
print("\nUsuwany dwie marki na dwa sposoby")
del auta["skoda"]
auta.pop("ford")
for marka in auta:
    print("Mamy %d samochodów marki %s" % (auta[marka],marka))



