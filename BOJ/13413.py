import sys
input = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        start = input().strip('\n')
        des = input().strip('\n')
        answer = []
        for i in range(len(start)):
            if start[i] != des[i]:
                answer.append(start[i])
        b_cnt = answer.count('B')
        w_cnt = answer.count('W')
        print(abs(b_cnt-w_cnt) + min(b_cnt,w_cnt))