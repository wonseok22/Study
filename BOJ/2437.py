from itertools import combinations
n = int(input())
x = input()
G = list(map(int,x.split()))
G.sort()
solve = [0 for i in range(sum(G))]
for i in range(len(G)):
    y = list(combinations(G,i+1))
    for j in range(len(y)):
        solve[sum(y[j])-1]=1
for i in range(1,len(solve)+1):
    if solve[i]==0:
        print(i+1)
        exit()