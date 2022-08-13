# 실패율 
# : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

# 스테이지 개수 N , 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return

# 5(스테이지개수)	[2, 1, 2, 6, 2, 4, 3, 3](스테이지 번호)	[3,4,2,1,5]
# 4	[4,4,4,4,4]	[4,1,2,3]

def solution(N, stages): # 5, [2, 1, 2, 6, 2, 4, 3, 3]
    a = len(stages) #스테이지에 도전하는 플레이어 수
    s = sorted(stages) # 오름차순 정렬 [1,2,2,2,3,3,4,6]
    answer = []

    for i in N : # N = 1,2,3,4,5
        if i in s :
            s.count(i) # 해당 스테이지에 도달한 사용자 수
            answer.append()



    return answer