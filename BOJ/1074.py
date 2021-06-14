import sys
input = sys.stdin.readline
ans = 0
def recursion(loc,leng):
    global ans
    x,y= loc
    if loc[0] == r and loc[1] == c:
        print(ans)
        exit()

    if leng == 1:
        ans += 1
        return

    if loc[0]<=r and r< loc[0]*leng and loc[1]<= c and c<loc[1]*leng:
        ans += leng*leng
        return

    recursion([x,y],leng//2)
    recursion([x,y + leng // 2],leng // 2 )
    recursion([x + leng// 2 ,y], leng//2)
    recursion([x + leng//2 , y + leng //2 ], leng//2)


if __name__ == '__main__':
    N,r,c = map(int,input().split())
    leng = 1
    for _ in range(N):
        leng *= 2
    recursion([0,0],leng)
