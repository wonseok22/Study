
N = input()
start = N
answer = 0
if N == "0":
    print(1)
    exit()
if int(N) < 10:
    start = "0" + start
while True:
    tmp = sum(map(int,N))
    N = N[-1] + str(tmp)[-1]
    answer += 1
    if N == start:
        print(answer)
        break
