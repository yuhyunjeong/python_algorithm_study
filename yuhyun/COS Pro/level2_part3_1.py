def solution(price, money):
    answer = 0
    if money < sum(price):
        answer = -1
    else:
        answer = money-sum(price)
    return answer