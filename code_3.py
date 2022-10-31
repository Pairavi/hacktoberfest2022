L=[]
while True :
    a=input("").split(" ")
    if a==["-1"]:
        break
    else:
        row=[int(x) for x in a]
        L.append(row)
    m=len(a)
 


n=len(L)                
transpose=""
for j in range(m):
    for k in range(n):
        try:
            transpose+=str(L[k][j])+" "
        except IndexError:
            transpose="Invalid Matrix"
            break
        else:
            pass
    transpose+="\n"
print(transpose)
        
                
