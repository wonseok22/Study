string = []
revFlag = True
answer = ""
for i in input():
    if i == "<":
        while string:
            answer += string.pop()
        answer += i
        revFlag = False
    elif i == ">":
        answer += i
        revFlag = True
    elif i == " " and revFlag == True:
        while string:
            answer += string.pop()
        answer += i
    else:
        if revFlag:
            string.append(i)
        else:
            answer += i
while string:
    answer += string.pop()
print(answer)