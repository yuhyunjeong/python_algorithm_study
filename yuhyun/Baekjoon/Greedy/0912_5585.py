money = [500, 100, 50, 10, 5, 1]

changes = 1000 - int(input())

result = 0

cnt = 0

while changes > 0:
    
    for i in range(len(money)):
           
        result = changes // money[i]
        changes -= result * money[i]
        cnt += result


print(cnt)

