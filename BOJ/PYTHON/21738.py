import sys
from collections import deque
input = sys.stdin.readline





if __name__ == "__main__":
    N,S,P = map(int,input().split())
    c = [0 for _ in range(N+1)]
    for i in range(S):
        c[i] = 1
    link = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        link[a].append(b)
        link[b].append(a)

    queue = deque()
    queue.append(P)
    cnt = 0
    c[P] = 1
    ans = []
    while queue:
        idx = queue.popleft()
        for i in link[idx]:
            if i <= S:
                cnt += 1
                ans.append(c[idx])
                if cnt == 2:
                    print(N-1-sum(ans))
                    exit()
            if c[i] == 0:
                c[i] = c[idx] + 1
                queue.append(i)