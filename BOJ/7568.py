import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    size = [list(map(int,input().split())) for _ in range(N)]
    ans = []
    for i in range(N):
        cnt = 0
        for x,y in size:
            if size[i][0] < x and size[i][1] < y:
                cnt += 1
        ans.append(str(cnt+1))
    print(' '.join(ans))