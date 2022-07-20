import sys
input= sys.stdin.readline

s = []
a,b = map(int,input().split())
for i in range(1000):
    for _ in range(i):
        s.append(i)
print(sum(list(s)[a-1:b]))
