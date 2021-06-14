from collections import Counter
c = Counter(input().lower()).most_common(2)
if c[0][1] > c[1][1]:
    print(c[0][0].upper())
else:
    print('?')
