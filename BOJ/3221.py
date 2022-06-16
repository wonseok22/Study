import sys
input = sys.stdin.readline

L,T  = map(int,input().split())
N = int(input())
ant = []
answer = []
for _ in range(N):
    pos, dir = input().split()
    ant.append([int(pos),dir])

for i in range(N):
    if ant[i][1] == "L": # 왼쪽으로 이동하는경우
        move = T+L-ant[i][0] # 개미가 이동한 칸
        if move < L: # 개미가 L보다 작은 길이를 이동한 경우
            answer.append(L-move)
        else:
            if (move//L) % 2 == 1: # 개미가 이동한 거리가 L의 홀수배수일 경우
                answer.append(move%L)
            else:
                answer.append(L - move%L)
    else: # 오른쪽으로 이동하는 경우
        move = T + ant[i][0]
        if move < L:
            answer.append(move)
        else:
            if (move//L) % 2 == 1:
                answer.append(L - move%L)
            else:
                answer.append(move%L)
answer.sort()
print(' '.join(map(str,answer)))