# import sys, re
# input = sys.stdin.readline
#
# S = input().strip()
# del_S = input().strip()
# while re.findall(del_S,S):
#     S = S.replace(del_S,"")
# print(S) if S else print("FRULA")


import sys
input = sys.stdin.readline

S = input().strip()
del_S = list(input().strip())
l = len(del_S)
last_word = del_S[-1]
answer = []
for i in S:
    answer.append(i)
    if i == last_word and answer[-l:] == del_S: # 폭발문자열을 찾은 경우
        for _ in range(l):
            answer.pop()
print(''.join(answer)) if answer else print("FRULA")
