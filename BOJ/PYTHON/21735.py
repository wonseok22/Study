import sys

input = sys.stdin.readline

def bf(curr,volume,cnt):
    if curr <= N-1:
        if cnt == M:
            ans.append(volume)
            return
    if curr == N-1:
        if cnt <= M:
            ans.append(volume)
            return
    if curr < N-1:
        bf(curr+1,volume+arr[curr+1],cnt+1)
    if curr < N-2:
        bf(curr+2,(volume//2)+arr[curr+2],cnt+1)
    return

if __name__ == "__main__":
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    ans = []
    bf(-1,1,0)
    print(max(ans))
