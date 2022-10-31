#program for finding whether number is prime or not

n=int(input(""))

while n>0: 
    if n>1 :
        for j in range(2,n) :
            if not(n%j) :              #if i divided by j
                print("non-prime ")
                break

        else:
            print("prime")


    elif n==1:
        print("non-prime")


    n=int(input(""))
