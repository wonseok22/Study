import sys
input = sys.stdin.readline



if __name__ == "__main__":
    N = list(map(int,input().strip()))
    ans = [0 for _ in range(len(N)+1)]
    if N[0] == 0:
        print(0)
    else:
        N = [0] + N
        ans[0] = 1
        ans[1] = 1
        for i in range(2,len(N)):
            x1 = N[i]
            x2 = N[i-1]*10 + N[i]
            if 0 < x1 < 10:
                ans[i] += ans[i-1]
            if 10 < x2 < 27:
                ans[i] += ans[i-2]
            ans[i] %= 1000000
        print(ans[len(N)-1])
