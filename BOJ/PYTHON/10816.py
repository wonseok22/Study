import sys
from collections import Counter
input  = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int,input().split()))
    M = int(input())
    find = list(map(int,input().split()))
    s = Counter(nums)
    for i in find:
        print(s[i],end = ' ')


