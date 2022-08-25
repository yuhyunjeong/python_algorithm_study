# 미완성

# 스택

def solution(order):
    answer = 0

    list = [1,2,3,4,5]
    sub = []
    
    for i in order:
        for j in list:
            if list[j]==order[i]:
                break
            list.remove(list[j])
            sub.append(list[j])


    return answer