import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        N,M = map(int,input().split())
        weight = deque(list(map(int,input().split())))
        cnt = 0
        check = weight.copy()
        for i in range(N):
            weight[i] = [weight[i],i]
        while weight:
            x = weight[0]
            if x[0] != max(check):
                weight.append(x)
                weight.popleft()
                check.append(check.popleft())
            else:
                cnt += 1
                weight.popleft()
                check.popleft()
                if x[1] == M:
                    print(cnt)
                    break
