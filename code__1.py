def getNum(a):                                      #function for obtain number from file
    try:
        fo=open(a,"r")                              #open file for reading only
        Num=int(fo.read())                          #read the file
        fo.close()                                  #close the opened file 
    except IOError:                                 #to handle if there is no such file  
        print("Invalid input.") 
    except ValueError:                              #if file contains string type elements
        print("Invalid input.")
    else:
        if 0<=Num<=20:                              #checking the range of Num
            return Num
        else:                                       
            print("Invalid input.")                   


def fibonacci(n):                                  #function to obtain fibonacci number
    if n<=1:                                       #F(n)=F(n-1)+F(n-2)   F(0)=0   F(1)=1
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    

def show(n,Fn):                            #function for display the n and F(n)
    print("Fibonacci(%d) = %d"%(n,Fn))
    

def saveFile(File,n,Fn):
    fr=open(File,"w")                          #open a file for writing only
    fr.write("Fibonacci(%d) = %d"%(n,Fn))      #write the output in the file
    fr.close()                                 #close the opened file
    

infile=input("")
n=getNum(infile)
if n!=None:                                        #for avioding errors if input file doesn't contain integer value in the given range
    show(n,fibonacci(n))
    saveFile("result.txt",n,fibonacci(n))

    
