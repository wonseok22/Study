N = int(input())
for i in range(N):
    G = []
    count=0
    num = int(input())
    for j in range(num):
        x,y=input().split()
        G.append((x,y))
    G.sort(key=lambda x : x[0], reverse=True )
    for x in range(len(G)):
        for y in range(x,len(G)):
            if G[x][1] > G[y][1]:
                count-=1
                break
        count+=1
    print(count)