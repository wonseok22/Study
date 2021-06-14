def solution(s):
    answer = 1000
    a = []
    if len(s) == 1:
        return 1
    for i in range(1, (len(s) // 2) + 1):
        check = [s[j:j + i] for j in range(0, len(s), i)]

        idx = 0
        flag = 0
        cnt = 0
        queue = []
        for text in check:
            if len(text) != i:
                cnt += len(text)
            else:
                if not queue:
                    queue.append(text)
                    cnt += i
                    idx+=1
                elif queue[-1] != text:
                    flag = 0
                    queue.append(text)
                    cnt += i
                    idx = 1
                elif queue[-1] == text and flag == 0:
                    flag = 1
                    cnt += 1
                    idx += 1
                    queue.append(text)
                elif queue[-1] == text and flag == 1:
                    idx += 1
                    if idx == 10:
                        cnt += 1
                    if idx == 100:
                        cnt += 1
                    if idx == 1000:
                        cnt += 1
                    queue.append(text)

        answer = min(answer, cnt)
    return answer

if __name__ == "__main__":
    s = "aaaaaaaaaabbbbbbbbbb"
    print(solution(s))
