import sys
from itertools import combinations
input = sys.stdin.readline

def ccw(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

if __name__ == "__main__":
    N = int(input())
    maps = [list(input()) for _ in range(N)]
    ans = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] != '.':
                ans.append([i,j])
    cnt = 0
    for value in combinations(ans,3):
        if ccw(value[0],value[1],value[2]) == 0:
            cnt +=1
    print(cnt)