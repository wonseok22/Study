import sys
input = sys.stdin.readline

X,Y = map(int,input().strip().split())

winRate=(100*Y)//X
start= 0
end = X
check = X
if winRate>=99:
    print(-1)
else:
    while start<=end:
        mid=(start+end)//2
        if (100*(Y+mid))//(X+mid)>winRate:
            check=mid
            end=mid-1
        else:
            start=mid+1
    print(check)