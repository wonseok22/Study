import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    for x,y in sorted([list(map(int,input().split())) for _ in range(N)],key = lambda x : (x[1],x[0])):
        print(x,y)
