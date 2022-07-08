import sys
input = sys.stdin.readline

L = int(input())
s = list(map(int,input().split()))
N = int(input())
answer = 0
if N in s:
    print(answer)
    exit()
s.sort()


