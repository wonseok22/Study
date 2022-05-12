N,L,R,X = map(int,input().split())
A = list(map(int,input().split()))
visited = 0b0
answer = set()
def bt(s, min_score, max_score, idx):
    global visited
    if L <= s and max_score - min_score >= X:
        answer.add(visited)
    for i in range(idx, N):
        if visited & (1 << i) == 0:
            visited ^= (1 << i)
            if s + A[i] <= R: bt(s+A[i], min(min_score, A[i]), max(max_score, A[i]), i+1)
            visited ^= (1 << i)
if N > 1:
    bt(0, 10**6 + 1, -10**6-1, 0)
    print(len(answer))
else:
    print(0)

