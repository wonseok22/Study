import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    A = sorted(list(map(int,input().split())))
    M = int(input())
    B = list(map(int,input().split()))
    for i in B:
        start = 0
        end = N-1
        flag = False
        while start <= end:
            mid = (start + end) // 2
            if A[mid] < i:
                start = mid + 1
            elif A[mid] > i:
                end = mid - 1
            else:
                flag = True
                print(1)
                break
        if not flag:
            print(0)