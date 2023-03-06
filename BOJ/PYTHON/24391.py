import sys
input = sys.stdin.readline

def find_parent(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent[x])
    return x

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N,M = map(int,input().split())
parent = [i for i in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    union_parent(a,b)
answer = -1
before = -1
for i in list(map(int,input().split())):
    p = find_parent(i)
    if p != before:
        before = p
        answer += 1
print(answer)

