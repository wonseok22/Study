import sys
input = sys.stdin.readline

def comb(count, x, start):
    global answer
    if count == K:
        tmp = 0
        for word in words:
            if word & x == word:
                tmp += 1
        answer = max(tmp, answer)
        # print(bin(x), tmp,count)

        return
    for i in range(start,21):
        x |= 1 << i
        comb(count+1, x, i+1)
        x &= ~(1 << i)

N, K = map(int,input().split())
words = [input().strip() for _ in range(N)]
K-=5
if K < 0:
    print(0)
    exit()

alphabet = dict()
alphabet_cnt = 0
for i in range(26):
    if chr(ord("a") + i) not in ["a","n","t","i","c"]:
        alphabet[chr(ord("a")+i)] = alphabet_cnt
        alphabet_cnt += 1
    else:
        alphabet[chr(ord("a")+i)] = -1
for idx,word in enumerate(words):
    wordToBin = 0
    for s in word:
        if alphabet[s] >-1:
            wordToBin |= (1 << alphabet[s])
    words[idx] = wordToBin
answer = 0
comb(0,0,0)
print(answer)
