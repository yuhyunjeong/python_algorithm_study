# 브루트포스(시간초과)
def solution(topping):
    answer = 0
    for i in range(len(topping)):
        if len(set(topping[:i])) == len(set(topping[i:])):
            answer += 1
    return answer