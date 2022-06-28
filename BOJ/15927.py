import sys,math
input = sys.stdin.readline

S = input().strip()
l = len(S)
if S == S[0] * l: print(-1)
elif S[:l//2][::-1] == S[math.ceil(l/2):]: print(l-1)
else: print(l)

