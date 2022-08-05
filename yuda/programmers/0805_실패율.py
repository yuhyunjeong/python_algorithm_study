def solution(N, stages):
    answer = {i:stages.count(i) for i in range(1, N + 1)}
    clear = len(stages)
    for i in range(1, N + 1):
        if clear > 0:
            answer[i] /= clear
        clear -= stages.count(i)
    return sorted(answer.keys(), key=lambda x:answer[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))