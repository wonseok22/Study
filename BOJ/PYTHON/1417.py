import sys
input = sys.stdin.readline


vote = []
for _ in range(int(input())):
    vote.append(int(input()))
if len(vote) == 1:
    print(0)
    exit()
first = vote[0]
vote = vote[1:]
answer = 0
while first <= max(vote):
    vote[vote.index(max(vote))] -= 1
    first += 1
    answer += 1
print(answer)