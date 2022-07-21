# n부터 m까지 자연수의 합

#1. 1부터 m까지의 합을 구합니다.
#2. 1부터 n-1까지의 합을 구합니다.
#3. 1번 단계에서 구한 값에서 2번 단계에서 구한 값을 뺍니다.

def func_a(k):
    sum = 0
    for i in range(k):
        sum += i+1
    
    # 풀이2
    # for i in range(k+1):
    #     sum += i

    return sum

def solution(n, m):
    sum_to_m = func_a(m)
    sum_to_n = func_a(n-1)
    answer = sum_to_m - sum_to_n
    return answer

result = solution(5, 10)
print(result)