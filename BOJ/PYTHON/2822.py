score = [[int(input()),i] for i in range(1,9)]
score.sort(reverse=True)
print(sum(i[0] for i in score[:5]))
print(' '.join(map(str,[i[1] for i in sorted(score[:5],key = lambda x : x[1])])))

