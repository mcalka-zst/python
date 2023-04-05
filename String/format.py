import os
os.system("cls")

age = 100
pension = 3000
text = "Jasio ma {} lat"
print(text.format(age))

text = "Jasio ma {} lat i {}zł emerytury"
print(text.format(age, pension))

text = "Jasio ma {0} lat i {1}zł emerytury"
print(text.format(age, pension))

text = "Jasio ma {1}zł emerytury i {0} lat"
print(text.format(age, pension))