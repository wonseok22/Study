import sys
input = sys.stdin.readline

N = int(input())
line = list(input().strip())
dna = dict()
answer = 10 ** 9
ans_word = ""
dna["A"] = 0
dna["G"] = 0
dna["T"] = 0
dna["C"] = 0
for l in line:
    dna[l] += 1
for i in dna:
    if dna[i] < answer:
        answer = dna[i]
        ans_word = i
print(answer)
print(ans_word * N)