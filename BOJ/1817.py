import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,M = map(int,input().split())
    weight = list(map(int,input().split()))
    curr = 0
    ans = 1
    if N == 0:
        print(0)
        exit()
    for i in weight:
        if i + curr > M:
            curr = i
            ans += 1
        else:
            curr += i
    print(ans)
