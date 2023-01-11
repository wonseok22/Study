import sys
from collections import Counter
input = sys.stdin.readline

n,d = map(int,input().split())
graph = list(map(int,input().split()))
# graph = sorted(graph,key = lambda x : (-graph.count(x), graph.index(x)))
graph = Counter(graph).most_common()
answer = 0

for value, fre in graph:
    while fre > d:
        fre -= (d-1)
        answer += 1
print(answer)