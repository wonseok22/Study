import sys
input = sys.stdin.readline
from itertools import permutations

N,M = map(int,input().split())
for value in permutations([i for i in range(1,N+1)],M):
    for j in value:
        print(j,end = ' ')
    print()

