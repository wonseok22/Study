left = 0
right = 1
answer = 0
acc = 1
N = int(input())
while left <= right:
    if acc == N:
        answer += 1
        right +=1
        acc += right
    elif acc < N:
        right += 1
        acc += right
    elif acc > N:
        acc -= left
        left += 1
print(answer)