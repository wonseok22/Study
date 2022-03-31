vowel = ["a","e","i","o","u"]
while True:
    cnt = 0
    S = input().lower()
    if S == "#":
        break
    for i in(S):
        if i in vowel:
            cnt += 1
    print(cnt)