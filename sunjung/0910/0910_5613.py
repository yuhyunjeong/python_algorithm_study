# 연산자의 우선 순위는 생각하지 않는다
result = int(input())
while True:
    symbol = input()
    if symbol == '=':
        break
    n = int(input())
    if symbol == '+': 
        result += n
    elif symbol == '-': 
        result -= n
    elif symbol == '*': 
        result *= n
    elif symbol == '/': 
        result //= n
print(result)