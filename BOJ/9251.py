import sys

input = sys.stdin.readline

S1 = input().strip()
S2 = input().strip()
l1 = len(S1)
l2 = len(S2)
LCS = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
for i in range(1,l1+1):
    for j in range(1,l2+1):
        if S1[i-1] == S2[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])
print(LCS[l1][l2])

