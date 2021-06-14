people = int(input())
x = input()
tall = x.split()
new_tall = []
for i in range(len(tall)):
    new_tall.append((i+1,int(tall[i])))
solve = [0 for i in range(people)]
cnt = 0
for i in range(len(new_tall)):
    for j in range(people):
        if solve[j] == 0:
            if cnt == new_tall[i][1]:
                solve[j] = i + 1
                cnt = 0
                break
            cnt += 1
for i in(solve):
    print(i,end=' ')