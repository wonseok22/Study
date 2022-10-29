def merge(left_list, right_list):
    result = []
    left_len = len(left_list)
    right_len = len(right_list)

    #왼쪽, 오른쪽 배열이 존재하는 동안
    while (left_len > 0 and right_len > 0):
        if left_list[0] <= right_list[0]:
            result.append(left_list[0])
            left_list = left_list[1:]
            left_len -= 1
        else:
            result.append(right_list[0])
            right_list = right_list[1:]
            right_len -= 1

    return result + left_list + right_list


def merge_sort(list):
    # 길이가 1 이하일 경우 배열을 반환
    if len(list) <= 1:
        return list

    # 배열을 왼쪽 절반, 오른쪽 절반으로 나눈다.
    mid = len(list)//2
    left_list = merge_sort(list[:mid])
    right_list = merge_sort(list[mid:])

    # merge 호출
    return merge(left_list, right_list)

def quick_sort(list):
    # 길이가 1 이하일 경우 배열을 반환
    if len(list) <= 1:
        return list

    # 배열을 왼쪽, pivot, 오른쪽으로 나누어 재귀호출한다.
    # 왼쪽 : pivot보다 작은 값
    # pivot : pivot과 같은 값
    # 오른쪽 : pivot보다 큰 값
    pivotpoint = list[len(list)//2]
    left, pivot, right = [], [], []
    for i in list:
        if i < pivotpoint:
            left.append(i)
        elif i > pivotpoint:
            right.append(i)
        else:
            pivot.append(i)
    return quick_sort(left) + pivot + quick_sort(right)


list = []
N = int(input())
for _ in range(N):
    list.append(int(input()))
for i in (quick_sort(list)):
    print(i)