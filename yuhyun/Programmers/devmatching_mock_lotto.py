def solution(lottos, win_nums):
    answer = []
    cnt = 0
    rank = [6,6,5,4,3,2,1]

    
    for i in lottos:

        for j in win_nums:

            if i == j:
                cnt += 1
 
    answer.append(rank[cnt + lottos.count(0)])
    answer.append(rank[cnt])
    
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))