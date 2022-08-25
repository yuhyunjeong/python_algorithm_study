#미완성

def solution(want, number, discount):
    answer = 0

    for i in range(discount):
        dis = [j for j in range(i,len(sum(number)))]
        if (set(want) & set(dis)) == set(want):
            answer+=1
        


    return answer

print(solution())