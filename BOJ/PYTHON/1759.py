
vowels = ["a","e","i","o","u"]
L,C = map(int,input().split())
alpha = sorted(list(input().split()))

def solution(s, l,currIndex ,vowelCnt, consCnt ):
    if l == L and vowelCnt > 0 and consCnt > 1:
        print(s)
        return
    for i in range(currIndex,C):
        if alpha[i] in vowels:
            solution(s+alpha[i], l+1, i+1, vowelCnt + 1, consCnt)
        else:
            solution(s+alpha[i], l+1, i+1, vowelCnt, consCnt + 1)

solution("",0,0,0,0)