import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    print(sorted(list(map(int,input().split())))[(N-1)//2])
