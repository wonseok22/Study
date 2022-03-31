import sys
input = sys.stdin.readline
dic = dict()
for _ in range(int(input())):
    S = input().strip()
    if S in dic:
        dic[S] += 1
    else:
        dic[S] = 1
m = [0,'']
for i in sorted(dic.keys()):
    if m[0] < dic[i]:
        m = [dic[i],i]
print(m[1])