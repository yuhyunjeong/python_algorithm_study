# 공항 방문객

# 1. 입력으로 주어진 배열에서 가장 많은 방문객 수를 찾습니다.
# 2. 1번 단계에서 찾은 값을 제외하고, 나머지 값들로 이루어진 새로운 배열을 만듭니다.
# 3. 2번 단계에서 만든 새로운 배열에서 가장 큰 방문객의 수를 찾습니다.
# 4. 1번 단계와 3번 단계에서 구한 값의 차이를 구합니다.

def func_a(arr, n):
    ret = []
    for x in arr:
        if x != n:
            ret.append(x)
    return ret

def func_b(a, b):
    if a >= b:
        return a - b
    else:
        return b - a

def func_c(arr):
    ret = -1
    for x in arr:
        if ret < x:
            ret = x
    return ret

def solution(visitor):
    max_first = func_c(visitor)
    visitor_removed = func_a(visitor, max_first)
    max_second = func_c(visitor_removed)
    answer = func_b(max_first, max_second)
    return answer

print(solution([4,7,2,9,3]))