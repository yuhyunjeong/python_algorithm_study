def solution(N, stages):
    answer = []

    players = len(stages)
    fail = []

    for i in len(stages):
        if N-stages[i] >= 0:
            answer[i]+=1

    answer.sort()
     

    return answer