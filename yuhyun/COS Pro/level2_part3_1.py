def solution(price, money):
    answer = 0
    if money < sum(price):
        answer = -1
    else:
        answer = money-sum(price)
    return answer

# 풀이 2
def solution(price, money):
    C = money - sum(price)
    return C if C >= 0 else -1