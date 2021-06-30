import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    l = list(map(int,input().split()))
    L = sorted(l)
    D = dict()
    for i in l:
        D[i] = 0
    prev = L[0]
    for i in range(1,len(L)):
        if  L[i] != prev:
            D[L[i]] = D[prev]+1
        else:
            D[L[i]] = D[prev]
        prev = L[i]
    for i in l:
        print(D[i],end= ' ')
