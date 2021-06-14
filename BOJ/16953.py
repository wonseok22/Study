def bfs(A,B):
    queue = []
    queue.append([A])
    cnt = 0
    while queue[-1]:
        queue.append([])
        for i in queue[cnt]:
            if i == B:
                return cnt+1
            if i*10 + 1 <= B:
                queue[-1].append(i*10+1)
            if i*2 <= B:
                queue[-1].append(i*2)
        cnt+=1
    return -1


if __name__ == "__main__":
    A,B = map(int,input().split())
    print(bfs(A,B))
