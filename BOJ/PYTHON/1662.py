from collections import deque

if __name__ == "__main__":
    string = input()

    q = deque()

    for i in range(len(string)):
        if string[i] != ")":
            if string[i] == "(":
                q.append(string[i])
            else:
                q.append(int(string[i]))
        else:
            length = 0
            while q:
                value = q.pop()
                if value == "(":
                    break
                else:
                    if value >= 10:
                        length += value - 10
                    else:
                        length += 1
            length = length * q[-1] + 10
            q.pop()
            q.append(length)

    answer = 0
    for i in range(len(q)):
        if q[i] >= 10:
            answer += q[i] - 10
        else:
            answer += 1
    print(answer)