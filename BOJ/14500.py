n,m=map(int, input().split())
maps=[]
for i in range(n):
  maps.append(list(map(int, input().split())))

tet=[[[0,0],[0,1],[0,2],[0,3]], #-
    [[0,0],[1,0],[2,0],[3,0]], #ㅣ
    [[0,0],[0,1],[1,0],[1,1]], #ㅁ
    [[0,0],[0,1],[0,2],[1,0]], #ㄱ
    [[0,0],[0,1],[0,2],[1,2]],
    [[0,0],[1,0],[1,1],[1,2]],
    [[0,2],[1,2],[1,1],[1,0]],
    [[0,1],[0,0],[1,0],[2,0]],
    [[0,0],[0,1],[1,1],[2,1]],
    [[0,0],[1,0],[2,0],[2,1]],
    [[0,1],[1,1],[2,1],[2,0]],
    [[0,0],[0,1],[0,2],[1,1]], #ㅜ
    [[0,1],[1,0],[1,1],[1,2]],
    [[0,0],[1,0],[1,1],[2,0]],
    [[1,0],[0,1],[1,1],[2,1]],
    [[0,1],[1,1],[1,0],[2,0]],
    [[0,0],[1,0],[1,1],[2,1]],
    [[0,1],[0,2],[1,1],[1,0]],
    [[0,0],[0,1],[1,1],[1,2]]]

result=0
for i in range(n):
  for j in range(m):
    for k in tet:
      try:
        a=maps[i+k[0][0]][j+k[0][1]]
        b=maps[i+k[1][0]][j+k[1][1]]
        c=maps[i+k[2][0]][j+k[2][1]]
        d=maps[i+k[3][0]][j+k[3][1]]
        temp=a+b+c+d
      except:
        temp=0
      result=max(result,temp)
print(result)