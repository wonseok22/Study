import sys
input = sys.stdin.readline

L,N,K = map(int,input().split())
charge = list(map(int,input().split()))
left = L-charge[-1]
right = L+1
answer = 0
while left < right:
    mid = (left+right)//2
    charge_cnt = 0
    curr_pos = mid
    for i in range(N-1):
        if curr_pos >= charge[i] and curr_pos < charge[i+1]:
            charge_cnt += 1
            curr_pos = charge[i]
    print(curr_pos, "pos", end=" ")
    print(mid, "mid", charge_cnt)
    if K >= charge_cnt:
        right = mid - 1
        answer = mid
    else:
        left = mid
print(answer)
