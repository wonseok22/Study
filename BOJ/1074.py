import sys
input = sys.stdin.readline
ans = 0

def recursion(x,y,leng):
    global ans
    if x == r and y == c:
        print(ans)
        exit()

    if leng == 1:
        ans += 1
        return

    if not (x <= r < x + leng and y <= c < y + leng):
        ans += leng*leng
        return

    recursion(x,y,leng//2)
    recursion(x,y + leng // 2,leng // 2 )
    recursion(x + leng// 2 ,y, leng//2)
    recursion(x + leng//2 , y + leng //2 , leng//2)


if __name__ == '__main__':
    N,r,c = map(int,input().split())
    leng = 2**N
    recursion(0,0,leng)
