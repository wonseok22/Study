import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,M = map(int,input().split())
    height = list(map(int,input().split()))
    start = 0
    end = max(height)
    while start<=end:
        mid = (start + end)//2
        length = 0
        for i in height:
            if i >= mid:
                length += i - mid
        if length < M:
            end = mid - 1
        elif length >= M:
            start = mid + 1
    print(end)

