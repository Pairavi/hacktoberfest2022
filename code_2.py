import math
n=4
m=3

L=[]
for i in range(n):
    a=input("").split(" ")
    row=[int(x)for x in a]
    if len(row)!=m:
        print("Input correct number of subject")
        break
    else:
        L.append(row)
        

for k in range(len(L)):
    total=0
    for j in range(len(L[k])):
        total+=L[k][j]
        average=total/m
    print("Total:",total,"Average:",round(average,1))
