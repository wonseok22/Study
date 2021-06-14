import sys
input = sys.stdin.readline

if __name__ == "__main__":
    board = input()
    answer = []
    cnt = 0
    flag = True
    for key in board:
        if key == 'X':
            cnt +=1
        else:
            if cnt % 2 == 1:
                print(-1)
                exit()
            while cnt >= 2:
                if cnt >= 4:
                    answer.append('AAAA')
                    cnt -= 4
                elif cnt >= 2:
                    answer.append('BB')
                    cnt -= 2
            answer.append('.')
    del answer[-1]
    print(''.join(answer))

