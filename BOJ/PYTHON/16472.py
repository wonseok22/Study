N = int(input())
s = list(input())
s_len = len(s)
start = 0
end = 1
sets = set(s[0])
l = 1
answer = []
while start < end:
    print(answer)
    print(sets)
    print(start,end)
    print()
    if l < N+1 and end < s_len:
        if s[end] not in sets:
            sets.add(s[end])
            l += 1
        end += 1
    else:

        answer.append(end - start)
        l -= 1
answer.append(end-start-1)
print(max(answer))


