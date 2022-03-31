N = int(input())
words = [input() for _ in range(N)]
answer = ''
for i in range(len(words[0])):
    check = words[0][i]
    flag = True
    for j in words:
        if check != j[i]:
            flag = False
            break
    if flag:
        answer += check
    else:
        answer += "?"
print(answer)
