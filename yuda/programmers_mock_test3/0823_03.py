# 구현
def solution(distance, scope, times):
    answer = distance
    for i in range(len(scope)):
        for j in range(min(scope[i]), max(scope[i]) + 1):
            T = j % sum(times[i])
            if T <= times[i][0] and T != 0:
                answer = min(answer, j)
    return answer