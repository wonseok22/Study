import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    t = sorted(list(map(int,input().split())))
    start = 0
    end = N-1
    ans = 0
    if N == 1:
        print(t[0])
        exit()
    if N%2 == 0:
        while start<end:
            ans = max(ans,t[start] + t[end])
            start += 1
            end -= 1
    else:
        ans = t[end]
        end -= 1
        while start<end:
            ans = max(ans, t[start] + t[end])
            start += 1
            end -= 1
    print(ans)