testCase = int(input())
for _ in range(testCase):
    R,S = input().split()
    answer = ''
    for i in S:
        answer += i*int(R)
    print(answer)