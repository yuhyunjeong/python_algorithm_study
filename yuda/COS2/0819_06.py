def solution(height, k):
    answer = 0
    n = len(height)
    for h in height:
        # 키가 더 큰 사람을 찾기 위해 >= -> >
        if h > k:
            answer += 1
    return answer