test_case = int(input())

for i in range(test_case):
    number = int(input())
    X = []
    for _ in range(number):
        X.append(input())
    K = X.sorted()
    answer = 'YES'
    for idx, val in enumerate(K):
        if idx == len(K) - 1:
            break
        if val in K[idx + 1]:
            answer = 'NO'
    print(answer)

