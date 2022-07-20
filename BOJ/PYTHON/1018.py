import sys
input = sys.stdin.readline

def cnt(lst):
    w_cnt = 0
    b_cnt = 0
    w_cnt1 = 0
    b_cnt1 = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                if lst[i][j] == 'W':
                    w_cnt += 1
                else:
                    b_cnt += 1
            else:
                if lst[i][j] == 'W':
                    w_cnt1 += 1
                else:
                    b_cnt1 += 1
    return min(64-(w_cnt+b_cnt1),64-(b_cnt+w_cnt1))

if __name__ == "__main__":
    N,M = map(int,input().split())
    board = [list(input().strip()) for _ in range(N)]
    ans = 64
    for i in range(N-7):
        for j in range(M-7):
            ans = min(ans,cnt([board[k][j:j+8] for k in range(i,i+8)]))
    print(ans)