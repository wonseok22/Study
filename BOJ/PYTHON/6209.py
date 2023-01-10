import sys
input = sys.stdin.readline



d,n,m = map(int,input().split())
land = sorted([int(input()) for _ in range(n)]) + [d]
start = 0
end = d
count = 0



