import random
import os
os.system("cls")
 
def randchar():
    nr= random.randint(65,91)
    if nr==91:
        char=" "
    else:
        char = chr(nr)
    return char

text =input("podaj tekst (duże litery i spacje): ")
text = text.upper()
ok=False
step=0
while(not ok):
    text2=""
    step+=1
    for i in range(len(text)):
        text2+=randchar()
    print("%d - %s" % (step,text2))
    if text==text2:
        ok=True
        print(f"Słowo {text} wylosowano w {step} kroku")