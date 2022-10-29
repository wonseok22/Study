from itertools import combinations
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N,K = map(int,input().split())
    if K < 5:
        print(0)
        exit()
    K -= 5
    l = [input().strip()[4:-4] for _ in range(N)]
    alpha = {}
    for i in range(97,96+27,1):
        alpha[chr(i)] = 0
    alpha['a'] = 1
    alpha['n'] = 1
    alpha['t'] = 1
    alpha['i'] = 1
    alpha['c'] = 1
    



