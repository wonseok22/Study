


for _ in range(int(input())):
    string = input()
    left = 0
    right = len(string)-1
    answer = 0
    while left < right:
        if string[left] != string[right]:
            del_left = string[:left] + string[left+1:]
            del_right = string[:right] + string[right+1:]
            if del_left == del_left[::-1] or del_right == del_right[::-1]:
                answer = 1
            else:
                answer = 2
            break
        else:
            left += 1
            right -= 1
    print(answer)
