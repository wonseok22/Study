# import sys
# from itertools import product
# input = sys.stdin.readline
#
#
# def backTracking(N,M,l):
#
# if __name__ == "__main__":
#     N,M = map(int,input().strip().split())


n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()
dfs(1)