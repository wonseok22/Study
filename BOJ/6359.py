for _ in range(int(input())):
    N = int(input())
    answer = 0
    rooms = [True for _ in range(N+1)]
    for i in range(1,N+1):
        check = i
        while check <= N:
            if rooms[check]:
                rooms[check] = False
            else:
                rooms[check] = True
            check += i
    for i in range(1,N+1):
        if not rooms[i]:
            answer += 1
    print(answer)
