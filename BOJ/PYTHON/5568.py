import sys
from itertools import permutations
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    card = [input().strip() for _ in range(n)]
    ans = []
    for idx in permutations(card,k):
        value = ''
        for key in idx:
            value += key
        ans.append(value)
    print(len(set(ans)))

