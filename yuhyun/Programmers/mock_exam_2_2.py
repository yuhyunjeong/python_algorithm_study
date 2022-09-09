def solution(topping):
    answer = -1

    result = []
    for value in topping:
        if value not in result:
             result.append(value)

    #print("중복 제거 전 : ", topping)
    #print("중복 제거 후 : ", result)


    return answer

# 브루트 포스 (시간 초과)

# 슬라이딩 윈도우 (연속한 경우) <-> 투 포인터 (연속 안한 경우)