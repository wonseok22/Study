import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    hi = list(map(int,input().split()))
    ai = list(map(int,input().split()))
    tree = []
    ans = 0
    for i in range(n):
        tree.append([hi[i],ai[i]])
    tree.sort(key = lambda x : x[1])
    for i in range(n):
        ans += tree[i][0]+(tree[i][1]*i)
    print(ans)