def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

N = int(input())
M = int(input())
answer = 0
minAnswer = M
first = True
for i in range(N,M+1):
    if isPrime(i):
        if first:
            minAnswer = i
            first = False
        answer += i
if answer == 0:
    print(-1)
    exit()
print(answer)
print(minAnswer)
