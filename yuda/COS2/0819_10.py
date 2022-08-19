def solution(arr, k):
    lst = []
    for x in arr:
        lst.extend(x)
    return sorted(lst)[k - 1]