import sys
input = sys.stdin.readline

N,M = map(int,input().split())
S = {input().strip() for _ in range(N)}
print(sum(1*(input().strip() in S) for _ in range(M)))