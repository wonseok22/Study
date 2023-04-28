import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solve(bullet, score):
    global N,K,answer
    if bullet == K:
        answer = max(answer,score)
        return

    for lane in range(N): # 몇 번째 라인 쏠지 정하기
        for col in range(N): # 몇번째 칸 쏠지 정하기
            hp = board[lane][col][0]
            max_hp = board[lane][col][1]
            if hp != 0:
                d = damage[bullet] # 현재 쏠 총알
                if max_hp > 9: # 보너스
                    board[lane][col][0] = 0
                    solve(bullet+1, score+hp)
                    board[lane][col][0] = hp
                elif d < hp: # 관통 실패
                    board[lane][col][0] = hp-d
                    solve(bullet+1, score)
                    board[lane][col][0] = hp
                elif d >= hp:
                    board[lane][col][0] = 0
                    tmp = [0 for _ in range(4)]
                    if max_hp > 3:
                        for i in range(4):
                            ax = lane + dx[i]
                            ay = col + dy[i]
                            if ax < 0 or ay < 0 or ax >= N or ay >= N or board[ax][ay][0] != 0: continue
                            tmp[i] = board[ax][ay]
                            board[ax][ay] = [max_hp//4, max_hp//4]
                    solve(bullet+1, score+max_hp)
                    board[lane][col][0] = hp
                    if max_hp > 3:
                        for i in range(4):
                            ax = lane + dx[i]
                            ay = col + dy[i]
                            if ax < 0 or ay < 0 or ax >= N or ay >= N or tmp[i] == 0: continue
                            board[ax][ay] = tmp[i]
                break



answer = 0
N = int(input())
K = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
target = [0 for _ in range(N)]
for i in range(N):
    for j in range(N):
        board[i][j] = [board[i][j], board[i][j]]

damage = list(map(int,input().split()))
solve(0,0)
print(answer)