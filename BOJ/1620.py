import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N,M = map(int,input().split())
    dic = dict()
    for i in range(N):
        name = input().strip()
        num = str(i+1)
        dic[name] = num
        dic[num] = name
    for j in range(M):
        q = input().strip()
        input().strip().split()
        if '0' <= q <= '200000':6
            print(q)