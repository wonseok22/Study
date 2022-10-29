import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        tree[b] = a
    A,B = map(int,input().split())
    parent_list = {}
    while A != 0: # A -> ROOT까지 모든 경로를 담음
        parent_list.add(A)
        A = tree[A]
    while True: # B-> ROOT까지 갈때, A -> ROOT의 경로와 만나는 부분 출력
        if B in parent_list: # A->ROOT의 경로와 만나는 부분
            print(B)
            break
        B = tree[B]
