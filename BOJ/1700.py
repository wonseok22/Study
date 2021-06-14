N, K = input().split()
X = list(map(int,input().split()))
min_time = 0
new_list = [ 0 for i in range(int(K)+1)]
for i in range(int(K)):
    new_list[X[i]] +=1
plug = []
mini = 101
m = 0
for i in range(int(K)):
    print(X[i])
    if len(plug)<int(N):
        new_list[X[i]] -= 1
        if X[i] not in plug:
            plug.append(X[i])
    else:
        if X[i] not in plug:
            mini = 101
            for j in plug:
                if mini>new_list[j]:
                    mini = new_list[j]
                    m=j
            plug.remove(m)
            new_list[X[i]] -= 1
            plug.append(X[i])
            min_time +=1
        else:
            new_list[X[i]] -=1
print(min_time)