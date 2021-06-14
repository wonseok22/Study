x = []
K = int(input())
for i in range(K):
    a = int(input())
    if a == 0:
        x.pop()
    else:
        x.append(a)
print(sum(x))