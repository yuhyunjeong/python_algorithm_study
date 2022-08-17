t = int(input())

for i in range(t):
    a , b , c = map(int, input().split())
    lst = [a,b,c]
    type = ''

    if max(lst) >= sum(lst , -max(lst)): # 삼각형이 만들어지지 않는 조건
        type = 'invalid!'

    elif a == b == c:
        type = 'equilateral'

    elif a == b or b == c or c == a:
        type = 'isosceles'
        
    else:
        type = 'scalene'
    
    print(f"Case #{i+1}: {type}")
