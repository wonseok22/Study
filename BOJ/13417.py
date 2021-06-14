from collections import deque

if __name__ == "__main__":
    testCase = int(input())
    for i in range(testCase):
        card = int(input())
        A = list(input().split())
        answer = deque([A[0]])
        del A[0]
        while A:
            c = A[0]
            del A[0]
            if c > answer[0]:
                answer.append(c)
            else:
                answer.appendleft(c)
        print(''.join(answer))
