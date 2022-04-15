import heapq as hq
answer = 0
N,C = map(int,input().split())
M = int(input())
sendList = [list(map(int,input().split())) for _ in range(M)]
package = [[] for _ in range(N+1)]
for f,t,c in sendList:
    package[f].append([t,c])
for p in package:
    p.sort()
carryWeight = 0
carryBox = []
for townNum in range(1,N+1):
    while carryBox and carryBox[0][0] == townNum:
        to,weight = hq.heappop(carryBox)
        answer += weight
        carryWeight -= weight
    for t,w in package[townNum]:
        if carryWeight < C:
            carryWeight += w
            if carryWeight > C:
                w -= carryWeight-C
                carryWeight = C
            hq.heappush(carryBox,(t,w))
        else:
            break
    print(carryBox)
    print(carryWeight)
    print(answer)
print(answer)

