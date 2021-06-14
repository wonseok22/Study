def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else :
        mid = len(lst) // 2
        left = lst[:mid] #리스트 슬라이스
        right = lst[mid:]
        return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

lst = list(map(int, input().split())) #data값을 띄어쓰기 구분으로 입력받는다
print(merge_sort(lst))