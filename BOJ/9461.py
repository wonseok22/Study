import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        ans = [1, 1, 1, 2, 2]
        N = int(input())-1
        start = 5
        if N > 4:
            while start<=N:
                ans.append(ans[-1]+ans[start-5])
                start += 1
        print(ans[N])

