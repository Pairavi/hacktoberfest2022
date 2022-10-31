#Program for finding number of abundant numbers from 2 to n(input number) inclusive

n=int(input("Input number: "))
t=0

if n>1:
    for i in range(2,n+1):
        s=0
        for j in range(1,i) :
            if (i%j==0) :
                s+=j

        if s>i :
            t+=1

    print("Number of abundant numbers from 1 to",n,"is",t)

else:
    print("Invalid Input ")
