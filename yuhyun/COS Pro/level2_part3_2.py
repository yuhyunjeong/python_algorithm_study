def solution(arr, k):
    answer = 0
    
    lst = []

    for i in arr:
        for j in i:
            lst.append(j)

    lst.sort()
    
    answer = lst[k-1]

    return answer