import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    ans = [i for i in sorted([int(input()) for _ in range(N)])]
    for i in ans:
        print(i)