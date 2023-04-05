from collections import Counter #liczy ilość wystąpień

names = ["Jasio", "Stasio","Franio","Piotruś", "Pawełek","Pioruś","Henio","Franio","Franio", "Piotruś"]
counter=Counter(names)
print(counter)
print(dict(counter)) #tworzymy słownik - w słowniku dane nie dublują się
print(dict(counter.most_common())) #sortujemy słownik
print(dict(counter.most_common(1))) #występujący najczęściej
print(dict(counter.most_common(2))) #dwa występujące najczęściej
