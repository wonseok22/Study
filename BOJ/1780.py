import sys
input = sys.stdin.readline

if __name__ == "__main__":
    K = int(input())
    board = [list(map(int,input().split())) for _ in range(K)]
