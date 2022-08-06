# 1

from re import S


def solution(s):
    answer = 0
    input = []

    for i in s:
        input.append(i)

        if input.count(i)==2:
         answer = int(i*3)
        
        input.sort()

    
    
    

    if not input:
        answer = -1
    

    return answer

# 2
def solution(levels):
    answer = 0
    lst = []

    top = int(len(levels) * 25 / 100)

    lst = levels[-top:]

    answer = lst[0]

    return answer


# 4
def solution(invitationPairs):
    answer = []

    score = {}
    for i in invitationPairs:
        score[i[0]] += 10
        score[1[0]] += i[1] * 3
        
        for j in i:
            j[0]



    return answer

# 5

def solution(tasks):
    answer = 0
    tasks.sort()
    cnt = 0 

    for i in tasks:
        if tasks.count(i) == 2 or 3:
            cnt += 1
        tasks.remove(i)
        answer = cnt
        if tasks.count(i) == 1:
            answer = -1


    return answer


# 6

from collections import defaultdict
def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = []
    name = []
    
    names_one.append(name)
    names_two.append(name)
    names_three.append(name)
    name.set()

    cnt = defaultdict(int)

    for i in name:
        cnt[i] += 

    

    return answer
