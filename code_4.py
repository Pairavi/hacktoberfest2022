A=[]
B=[]

def matrix(r,c):
    #return matrix A,matrix B as lists
    global A
    global B
    while True:
        a=input("").split()
        try:
            row=[int(x) for x in a]                      #convert the list of strings to  list of integers
        except ValueError:
            print("error")
            break
        else:
            if c==len(row) and len(A)<r:                 #1st matrix is A 1st r rows belong to A
                A.append(row)
            elif c==len(row) and len(A)>=r and len(B)<r: 
                B.append(row)
                if len(B)==r:
                    break
            else:
                print("Invalid Matrix")
                A=[]                                     
                B=[]
                break
    return A,B

def transpose_matrix(mylist,r,c):
    #this prints transpose of matrix
    transpose=[]
    for j in range(c):
        Row=[]
        for k in range(r):
            try:
                Element=mylist[k][j] 
            except IndexError:
                transpose="Invalid Matrix"
                break
            else:
                Row.append(Element)
        if transpose=="Invalid Matrix":
            break
        else:
            transpose.append(Row)
    return transpose

def product_matrices(M1,M2):
    #product 2 matrices and return them
    product=""
    if len(M1[0])==len(M2):
        for i in range(len(M1)):                        
            for j in range(len(M2[0])):
                p=0
                for k in range(len(M1[i])):
                     p+=M1[i][k]*M2[k][j]
                product+=(str(p)+" ")
            product+="\n"
        
    return product   
            
            
            
        
Row,Column=input("Enter the dimension:").split(",")
while True:
    try:
        R=int(Row)
        C=int(Column)
    except ValueError:
        print("Row and Column should be integers")
        break
    else:
        print(" Enter Matrix A:")
        matrix(R,C)
        if A==[] or B==[]:
            break
        else:
            print("Enter Matrix B:")
            transpose=transpose_matrix(B,R,C)
            print(product_matrices(A,transpose))
            break
