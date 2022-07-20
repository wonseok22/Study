import sys
import heapq as hq
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    heep = []
    for _ in range(N):
        value = int(input())
        if value == 0:
            if heep:
                print(hq.heappop(heep)[1])
            else:
                print(0)
        else:
            hq.heappush(heep,[abs(value), value])
