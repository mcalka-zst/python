import operator
import os

os.system("cls")

tab1=[4,7,-3,1,0,6,5,11,-67]
tab1.sort()
print(tab1)
#-------------------------------------------
print(sorted([4,7,-3,1,0,6,5,11,-67]))
#-------------------------------------------
tab2=[4,7,-3,1,0,6,5,11,-67]
tab2.sort(reverse=True)
print(tab2)
#-------------------------------------------
tab3=[[4,7],[-3,1],[0,-6],[5,11]]
tab3.sort()
print(tab3)
#-------------------------------------------
tab4=[[4,7],[-3,1],[0,-6],[5,11]]
tab4.sort(key = operator.itemgetter(1))
print(tab4)

#-------------------------------------------
tab5=[[4,7],[-3,1],[0,-6],[5,11]]
tab5=sorted(tab5, key = operator.itemgetter(1))
print(tab5)
