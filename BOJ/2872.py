import sys
input = sys.stdin.readline

if __name__ == "__main__":
    books = [int(input()) for _ in range(int(input().strip('\n')))]
    max = books[0]
    cnt = 0
    for i in books[1:]:
        if i > max:
            if max + 1 != i:
                cnt += 1
            max = i
        else:
            cnt += 1
    print(cnt)
