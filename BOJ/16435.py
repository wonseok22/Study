import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,L = map(int,input().split())
    h = sorted(list(map(int,input().split())))
    for i in range(N):
        if h[i] <= L:
            L += 1
        else:
            break
    print(L)

