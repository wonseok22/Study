import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
inorder = list(map(int,input().split()))
postorder = list(map(int,input().split()))
answer = []
index = [0] * (N+1)
for i in range(N):
    index[inorder[i]] = i

def preorder(s1,e1,s2,e2):
    if s1 > e1 or s2 > e2:
        return
    root = postorder[e2]
    rootIdx = index[root]
    answer.append(root)
    leftLength = rootIdx-s1
    preorder(s1, rootIdx-1, s2, s2 + leftLength - 1)
    preorder(rootIdx+1, e1, s2 + leftLength , e2-1)
preorder(0,N-1,0,N-1)
print(' '.join(list(map(str,answer))))