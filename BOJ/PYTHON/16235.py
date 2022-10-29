from collections import deque
import sys
input = sys.stdin.readline
def spring():
    for i in range(n):
        for j in range(n):
            len_t = len(t[i][j])
            for k in range(len_t):
                if t[i][j][k] <= no[i][j]:
                    no[i][j] -= t[i][j][k]
                    t[i][j][k] += 1
                else:
                    for _ in range(k, len_t):
                        no[i][j] += t[i][j].pop() // 2
                    break
def fall():
    for i in range(n):
        for j in range(n):
            for k in t[i][j]:
                if k % 5 == 0:
                    for l in range(8):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < n and 0 <= y < n:
                            t[x][y].appendleft(1)
            no[i][j] += s[i][j]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]
n, m, k = map(int, input().split())
s = []
t = [[deque() for i in range(n)] for i in range(n)]
no = [[5] * n for i in range(n)]
for i in range(n):
    s.append(list(map(int, input().split())))
for i in range(m):
    x, y, z = map(int, input().split())
    t[x - 1][y - 1].append(z)
for i in range(k):
    spring()
    fall()
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(t[i][j])
print(cnt)