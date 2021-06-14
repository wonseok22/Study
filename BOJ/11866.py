import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    N,K = map(int,input().split())
    cnt = deque([i+1 for i in range(N)])
    ans = []
    for i in range(K-1):
        cnt.append(cnt.popleft())
    while cnt:
        ans.append(cnt.popleft())
        if not cnt:
            break
        for i in range(K-1):
            cnt.append(cnt.popleft())
    print("<" + ', '.join(map(str,ans))+">")

