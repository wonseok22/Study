vowels = ["a","e","i","o","u"]
def c(s):
    vCnt = 0
    s1 = 0
    s2 = 0
    stack = []
    for i in s:
        if stack:
            if stack[-1] == i:
                if i != "e" and i != "o":
                    return False
        stack.append(i)
        if i in vowels:
            vCnt += 1
            s1 += 1
            s2 = 0
        else:
            s1 = 0
            s2 += 1
        if s1 == 3 or s2 == 3:
            return False
    if vCnt == 0:
        return False
    else:
        return True

while True:
    pw = input()
    if pw == "end":
        break
    if c(pw):
        print("<{}> is acceptable.".format(pw))
    else:
        print("<{}> is not acceptable.".format(pw))