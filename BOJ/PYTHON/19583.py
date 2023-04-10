import sys

input = sys.stdin.readline

S,E,Q = input().split()
S = int(S.split(":")[0])*60 + int(S.split(":")[1])
E = int(E.split(":")[0])*60 + int(E.split(":")[1])
Q = int(Q.split(":")[0])*60 + int(Q.split(":")[1])
check = set()
answer = 0
while True:
    try:
        time, name = input().split()
        time = int(time.split(":")[0])*60 + int(time.split(":")[1])
        if time <= S:
            check.add(name)
        if E <= time <= Q and name in check:
            check.remove(name)
            answer += 1
    except:
        break
print(answer)