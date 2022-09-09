def solution(arr, K):
    answer = 10000
    arr.sort()
    for i in range(len(arr) - K + 1):
        answer = min(answer, arr[i + K - 1] - arr[i])
    return answer

# def solution(arr, K):
    
#     answer = 0

#     lst = [0 for i in range(K)] 

#     for i in arr:
        



#     return answer