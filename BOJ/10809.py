dic = {}
for i in range(97,123):
    dic[chr(i)] = -1
n = input()
for key in range(len(n)-1,-1,-1):
    dic[n[key]] = key
for i in list(dic.values()):
    print(i,end=' ')
