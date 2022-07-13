
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    ans = -float("inf")
    if N > M :
        for i in range(N-M+1):
            s = 0
            for j in range(M):
                s += A[j+i] * B[j]
            ans = max(s,ans)
    elif M > N:
        for i in range(M-N+1):
            s = 0
            for j in range(N):
                s += A[j] * B[j+i]
            ans = max(s,ans)
    else:
        for j in range(N):
            s += A[j] * B[j]
        ans = s
    print("#{}".format(test_case),ans)
    # ///////////////////////////////////////////////////////////////////////////////////