
if __name__ == '__main__':
    numbers = input().split('-')
    s = []
    for value in numbers:
        s.append(sum(list(map(int,value.split('+')))))
    print(s[0] - sum(s[1:]))


