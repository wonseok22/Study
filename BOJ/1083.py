global zeroCnt
global oneCnt
def fibonacci(N):
    global zeroCnt
    global oneCnt
    if N == 0:
        zeroCnt +=1
        return 0
    elif N == 1:
        oneCnt +=1
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

testCase = int(input())
for i in range(testCase):
    zeroCnt = 0
    oneCnt = 0
    fibonacci(int(input()))
    print(zeroCnt,oneCnt)