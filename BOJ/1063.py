
K,S,N = input().split()
move = {
    "R" : [0,1],
    "L" : [0,-1],
    "B": [1, 0],
    "T": [-1, 0],
    "RT": [-1, 1],
    "LT": [-1, -1],
    "RB": [1, 1],
    "LB": [1, -1]
}
query = []
for _ in range(int(N)):
    query.append(input())
K = [8-int(K[1]),ord(K[0])-ord("A")]
S = [8-int(S[1]),ord(S[0])-ord("A")]
for i in query:
    if 0<=K[0]+move[i][0]<8 and 0<=K[1]+move[i][1]<8:
        K[0] += move[i][0]
        K[1] += move[i][1]
        if K == S:
            if 0 <= S[0] + move[i][0] < 8 and 0 <= S[1] + move[i][1] < 8:
                S[0] += move[i][0]
                S[1] += move[i][1]
            else:
                K[0] -= move[i][0]
                K[1] -= move[i][1]
print(chr(K[1]+65)+str(8-K[0]))
print(chr(S[1]+65)+str(8-S[0]))