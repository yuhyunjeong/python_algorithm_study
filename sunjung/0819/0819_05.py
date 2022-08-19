def solution(arr, k): #arr는 2차원배열, 자연수 k
    #arr에서 k번째로 작은수를 찾아서 return
    answer = 0
    list_1 = []
    for i in range (len(arr)) : #len(2차원배열) : 행의 수 
        for j in range (4):
            list_1.append(arr[i][j])
            
    list_2 = sorted(list_1)
    # 0 1 2 3 4 
    answer = list_2[k-1]    

    return answer