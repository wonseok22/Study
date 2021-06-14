import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':
    N,K = map(int,input().split())
    arr = deque([i for i in range(1,N+1)])
    ans = []
    while arr:
        for _ in range(K-1):
            arr.append(arr.popleft())
        ans.append(str(arr.popleft()))
    print("<",", ".join(ans),">",sep = '')

