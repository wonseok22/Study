x = []
for i in range(int(input())):
    a,b = input().split()
    x.append([a,b])
d = sorted(x , key = lambda x : (x[0], x[1]))
for c in d:
    print(c[0],c[1])
