import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,M = map(int,input().split())
    addr = {}
    for _ in range(N):
        addrs,pw = input().split()
        addr[addrs] = pw
    for _ in range(M):
        ad = input().strip()
        if addr[ad]:
            print(addr[ad])
