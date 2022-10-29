x = []
for i in range(int(input())):
    y= input()
    x.append(y)

x = list(set(x))
x.sort()
x.sort(key = len)
for c in x:
    print(c)
