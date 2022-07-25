# 총점

# 1. 모든 과목 점수의 합을 구합니다.
# 2. 최고 점수를 구합니다.
# 3. 최저 점수를 구합니다.
# 4. (모든 과목 점수의 합) - (최고 점수) - (최저 점수)의 값을 return 합니다.

def func_a(s):
    ret = 0
    for i in s:
        if i > ret:
            ret = i
    return ret

def func_b(s):
    ret = 0
    for i in s:
        ret += i
    return ret

def func_c(s):
    ret = 101
    for i in s:
        if i < ret:
            ret = i
    return ret


def solution(scores):
    sum = func_b(scores)
    max_score = func_a(scores)
    min_score = func_c(scores)
    return sum - max_score - min_score

result = solution([50,35,78,91,85])
print(result)