from collections import deque

answer = 0
for _ in range(int(input())):
    s = input()
    queue = deque()  # 연속된 단어를 하나만 쓴 가공된 문자열
    check = set() # 이미 나왔던 글자인지 체크하기 위함
    queue.append(s[0]) # 첫 글자는 무조건 넣어도 됨 -> if queue: 문을 안쓰려고 넣은 것

    # 주어진 문자의 2번째 글자부터 연속된 문자는 거르고 queue에 넣음
    for i in s[1:]:
        if queue[-1] != i:
            queue.append(i)

    #queue에서 check로 한 글자씩 옮기며 이미 있는 글자일경우 분기
    while queue:
        x = queue[0]
        if x in check:
            break
        else:
            queue.popleft()
            check.add(x)

    #queue의 모든 글자가 check로 들어간 경우 정답 1증가
    if not queue:
        answer += 1
print(answer)