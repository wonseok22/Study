def binarySearch(a):
    start = 0
    end = M-1
    result = 0
    while start <= end:
        mid = (start+end) // 2
        if B[mid] < a:
            start = mid + 1
            result = mid
        else:
            end = mid-1
    return result + 1

for _ in range(int(input())):
    N, M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    answer = 0
    for i in A:
        if i > B[0]:
            t =  binarySearch(i)
            answer += t
    print(answer)
