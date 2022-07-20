def isPalindrome(str):
    left_false = False
    right_false = False
    for i in range(len(str) // 2):
        if str[i] != str[len(str) - 1 - i]:
            for j in range(i, len(str) // 2):
                if str[j + 1] != str[len(str) - 1 - j]:
                    left_false = True

            for j in range(i, len(str) // 2):
                if str[j] != str[len(str) - 1 - j - 1]:
                    right_false = True

            if left_false and right_false:
                return 2
            elif left_false or right_false:
                return 1

    return 0

if __name__ == "__main__":
    T = int(input())
    name = []
    for _ in range(T):
        name.append(input())
    for M in name:
        print(isPalindrome(M))