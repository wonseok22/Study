import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,M = map(int,input().split())
    card = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                s = card[i] + card[j] + card[k]
                if s <= M:
                    ans = max(ans,s)
    print(ans)