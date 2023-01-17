import sys
input = sys.stdin.readline

N = int(input())
vertex = [0] + list(map(int,input().split()))
edge = [[[] for _ in range(N+1)]]
for i in range(N):
    p,c = map(int,input().split())
    edge[i+1].append([p,c])
tree = []
def dfs(node):
    
