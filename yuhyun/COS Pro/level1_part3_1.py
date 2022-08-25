from re import I


def solution(garden):
    answer = 0
    cnt = 0

    for i in range(len(garden)):
        for j in range(len(garden[i])):
            
            if garden.count(1) == len(garden)*len(garden[i]):
                break

            if garden[i][j] == 1:
                garden[i] = 1
                garden[][j] = 1
                
                answer += 1
  
    return answer

print(solution([[0,0,0],[0,1,0],[0,0,0]]))