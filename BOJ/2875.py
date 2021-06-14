a,b,k = map(int,input().split())
count=0
while a+b>=k and b>=0 and a>=0:
        count += 1
        a=a-2
        b=b-1
print(count-1)
