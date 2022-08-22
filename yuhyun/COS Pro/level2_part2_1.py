def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        if h > k:
            answer += 1
    return answer

print(solution([165, 170, 175, 180, 184], 175))