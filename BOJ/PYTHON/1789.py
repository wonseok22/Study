s= int(input())
if s==1 : 
    print(1)
    exit()

n=0
for i in range(1,s) :
    n+=i    
    if n==s :
        print(i)
        break    
    elif n>s : 
        print(i-1)
        break
