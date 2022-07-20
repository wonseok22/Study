import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n,k = map(int,input().split())
    num = deque(list(input().strip()))
    ans = [num.popleft()]
    while num and k > 0:
        if ans[-1] > num[0]:
            ans.append(num.popleft())
        else:
            ans.pop()
            ans.append(num.popleft())
            k-=1

    print(''.join(ans+list(num)))
