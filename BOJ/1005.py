import sys
input = sys.stdin.readline

if __name__ =="__main__":
    for _ in range(int(input())):
        N,K = map(int,input().split())
        D = list(map(int,input().split()))
        arr = [[] for _ in range(N+1)]
        for _ in range(K):
            x,y = map(int,input())
            arr[x].append(y)
        target = int(input())
        ans = 0
        dp = [0 for _ in range(N)]

