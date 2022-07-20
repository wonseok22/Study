N,K = map(int,input().split())
answer = []

def backTraking(n,s):
    if n == N:
        answer.append(s)
    if n > N:
        return
    for i in range(1,4):
        backTraking(n+i,s+str(i))

backTraking(0,"")
if K <= len(answer):
    print('+'.join(list(sorted(answer)[K-1])))
else:
    print(-1)