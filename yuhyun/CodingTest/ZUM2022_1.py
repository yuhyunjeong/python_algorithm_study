# 1. 임의의 자연수 n으로 나누었을 때, 그 몫과 나머지가 같아지는 모든 자연수를 더한 값

def solution(n):
    answer = 0

    # i = 1

    # while True:
        
    #     if i // n == i % n:
    #         answer += i
    #     i += 1
        
    for i in range(1, n):
        answer += (n*i + 1)

    return answer

# 2.
def solution(data):
    answer = [data[0][0]]
    arr = []
    arr2 = []
    n = 0

    for i in range(1,len(data)):
        
        if data[i][1] <= data[0][2]:
            
            if data[i][0] not in arr:
                arr.append(data[i])
                n += data[i][1]
        arr.sort(key=lambda arr : arr[2])
       

    answer.extend(arr)

    for i in range(len(answer),len(data)):
        
        if data[i][1] <= n:
            
            if data[i][0] not in arr:
                arr2.append(data[i])
                n += data[i][1]
                
        arr2.sort(key=lambda arr2 : arr2[2])
       

    answer.extend(arr2)


    return answer

# 3. 두 막대를 선택했을때 물이 최대로 차오를 수 있는 영역의 넓이

def solution(histogram):
    answer = -1
    lst = []
    
    for i in range(len(histogram)):

        for j in range(i,len(histogram)):

            result = (j - i - 1) * min(histogram[i],histogram[j])
            lst.append(result)
        
    answer = max(lst)
    
    return answer

# 4.
def solution(grid):
    answer = []

    max_count = 0
    count = 0

    for i in range(0, len(grid)-1):
        for j in range(0, len(grid[i])-1):
            if grid[i][j] == grid[i][j+1]:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                    count = 0

    return max_count