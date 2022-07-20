x  = []
T,g = input().split()
for i in range(int(T)):
    a=int(input())
    x.append([a,i])
x.sort(key = lambda x : x[0])
print(x)
for i in range(int(g)):
    m,n = input().split()
    for z in range(int(T)):
        if int(m)-1<=x[z][1] and x[z][1]<=int(n)-1:
            print(x[z][0])
            break