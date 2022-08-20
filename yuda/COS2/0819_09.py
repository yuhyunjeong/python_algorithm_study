def solution(price, money):
    C = money - sum(price)
    return C if C >= 0 else -1