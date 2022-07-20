import sys
input = sys.stdin.readline

for i in range(1,int(input().strip())+1):
    N = int(input())
    answer = 0
    for _ in range(N):
        x,y = map(int,input().split())
        r = (x**2 + y**2)**(1/2)
        answer += (11-(r//20-1)%11)
    print("#{}".format(i),int(answer))