from collections import deque

def bfs(start):
    X = start
    if M in queue[0]:
        print(i)
        print(visited[M])
        exit()
    if 0 < X <= 100000:
        #if visited[X-1] == 0:
        queue[-1].append(X-1)
        visited[X-1] +=1
    if 0 <= X < 100000:
        #if visited[X+1] == 0:
        queue[-1].append(X+1)
        visited[X+1] += 1
    if X*2 <= 100000:
        #if visited[X*2] == 0:
        queue[-1].append(X*2)
        visited[X*2] += 1

if __name__ == "__main__":
    N,M = map(int,input().split())
    visited = [0 for _ in range(100001)]
    queue = deque([])
    queue.append(deque([N]))
    i=0
    while queue[-1]:
        queue.append(deque([]))
        #print(queue)
        for z in queue[0]:
            bfs(z)
        queue.popleft()
        i+=1