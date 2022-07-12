import sys
input = sys.stdin.readline

N,K = map(int,input().split())
nums = list(map(int,input().split()))

left, right = 0, 10**5 * 20 + 1
answer = 0
while left <= right:
    mid = (left + right)//2
    total_score, divided_group = 0, 0 # 현재 그룹의 시험점수 총합, 그룹의 개수

    for i in nums: # 시험지의 순서가 있으므로 선형탐색으로 접근
        if total_score + i >= mid:  # 현재까지 더한 시험지의 점수가 최소값의 후보인 mid를 넘었을 경우 그룹을 나눠야 하므로 그룹 개수를 +1 현재 그룹의 총합을 0으로 초기화
            total_score = 0
            divided_group += 1
        else:
            total_score += i

    if divided_group < K: # K 개보다 적은 그룹인 경우 최솟값의 범위를 증가시켜야함
        right = mid - 1
    elif divided_group == K: # K개인 경우 정답 후보
        answer = max(mid,answer)
        left = mid + 1
    else: # K개보다 많은 경우 최솟값의 범위를 감소시켜야함
        left = mid + 1
print(answer)
