import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        c = deque(list(input().strip()))
        N = int(input())
        arr = list(input().strip())
        print(arr)