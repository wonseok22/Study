

if __name__ == "__main__":
    treelen = int(input())
    T = list(map(int,input().split()))
    d_node = int(input())
    tree = {}
    for i in range(treelen):
        if i == d_node or T[i] == d_node:
            continue
        if T[i] in tree:
            tree[T[i]].append(i)
        else:
            tree[T[i]] = [i]
    res = 0
    if -1 in tree:
        que = [-1]
    else:
        que = []
    while que:
        node = que.pop()
        if node not in tree:
            res +=1
        else:
            que += tree[node]
    print(res)
