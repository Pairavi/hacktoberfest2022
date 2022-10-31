#Program to encrypt message

n=input("Enter message:")
m=int(input(" Enter base: "))
L1=[]
s=''

if (1<m<=10) :
    for i in n:
        L=[]
        a=ord(i)
        while a>=m :
            t=a%m
            L.append(str(t))
            a=a//m

        else:
            L.append(str(a))

        L.reverse()
        L1.extend(L)
            
            
    for k in L1:
        s+=k

    print(s)

else:
    print("Not available")
