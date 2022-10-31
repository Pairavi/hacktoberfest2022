str_list=input().split()
List=[]
for i in str_list:
    a=float(i)
    List.append(a)

maximum=max(List)
minimum=min(List)

for i in str_list:            
    if float(i)==minimum :
        print("Minimum =",i)
        break
    
for i in str_list:
    if float(i)==maximum:
        print("Maximum =",i)
        break
    
