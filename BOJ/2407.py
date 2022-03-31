from itertools import combinations
import sys
input = sys.stdin.readline


if __name__ =="__main__":
    N,M = map(int,input().split())
    ans = 1
    for i in range(N,N-M,-1):
        ans *= i
    for i in range(M,0,-1):
        ans //= i
    print(ans)
