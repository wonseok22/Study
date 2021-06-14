import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        H,W,N = map(int,input().split())
        X = N % H
        Y = (N // H) +1
        if X == 0:
            X = H
            Y -= 1
        print(X*100+Y)