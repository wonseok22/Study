import sys
input = sys.stdin.readline

month = [0, ]

for _ in range(int(input())):
    B, C = map(int,input().split())
    book = []
    for _ in range(B):
        code, start_ymd, start_time, end_ymd, end_time = input().split()
        start_y, start_m, start_d = map(int,start_ymd.split())
        end_y, end_m, end_d = map(int, end_ymd.split())
        book.append([code, (start_y-2013)*525600, start_m * ])