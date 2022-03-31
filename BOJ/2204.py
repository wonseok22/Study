from copy import deepcopy

hile True:
    N = int(input())
    if N == 0:
        break
    words = []
    deepcopy(A)
    for i in range(N):
        tmp = input()
        words.append([tmp.lower(),tmp])
    print(sorted(words,key = lambda x : x[0])[0][1])