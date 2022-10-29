def rotate(board, key_len): #열쇠 시계방향으로 90도 회전
    tmp = [[0 for _ in range(key_len)] for _ in range(key_len)]
    for i in range(key_len):
        for j in range(key_len):
            tmp[j][key_len - i - 1] = board[i][j]
    return tmp


def check(key, lock, key_len, lock_len):
    arr = [[0 for _ in range(2 * (lock_len - 1) + key_len)] for _ in range(2 * (lock_len - 1) + key_len)]

    #열쇠를 자물쇠의 크기만큼 확장
    for i in range(key_len):
        for j in range(key_len):
            arr[lock_len + i - 1][lock_len + j - 1] = key[i][j]

    #확장한 열쇠에서 왼쪽 위의 자표를 (0,0)부터 (key_len + lock_len -1, key_len + lock_len -1)까지 탐색
    for a in range(lock_len + key_len - 1):
        for b in range(lock_len + key_len - 1):
            check = True
            for i in range(lock_len):
                for j in range(lock_len):
                    check = check and (arr[a + i][b + j] != lock[i][j])
            if check: #모든 홈이 일치한다면 참값을 반환
                return True

    return False


def solution(key, lock):
    answer = False
    key_len = len(key)
    lock_len = len(lock)
    for _ in range(4): # 4번 회전시켜 각 케이스 확인
        if check(key, lock, key_len, lock_len):
            return True#모든 모양에 대해 열쇠와 자물쇠의 홈이 일치하는지 확인
        key = rotate(key, key_len) # 열쇠 회전
    return False