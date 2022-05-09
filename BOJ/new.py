# import sys
# sys.setrecursionlimit(10**7)
answer = 10**9
target_alp = 0
target_cop = 0
problem = []
def rec(alp, cop, time):
    global answer,target_alp, target_cop
    print(alp, cop, time)
    if alp >= target_alp and cop >= target_cop:
        print(time)
        answer = min(answer,time)
        return
    if time < answer:
        for i in problem:
            if i[0] <= alp and i[1] <= cop:
                rec(alp + i[2], cop + i[3], time + i[4])
            else:
                if alp < i[0] and cop >= i[1] :
                    t1 = i[0] - alp
                    rec(i[0], cop, time + t1)
                elif alp >= i[0] and cop < i[1] :
                    t2 = i[1] - cop
                    rec(alp, i[1], time + t2)
                elif alp < i[0] and cop < i[1]:
                    t1 = i[0] - alp
                    t2 = i[1] - cop
                    rec(i[0], i[1], time + t1 + t2 )

def solution(alp, cop, problems):
    global answer,target_cop,target_alp, problem
    problem = problems
    for x in problems:
        target_alp = max(target_alp, x[0])
        target_cop = max(target_cop, x[1])
    rec(alp, cop,0)
    print(answer)
    return answer
solution(0,0,[[0,0,0,1,2],[4,5,3,1,2],[4,11,4,0,2],[100,4,0,4,2]])