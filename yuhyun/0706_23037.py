# 풀이 1
n = input()
sum=0

for i in range(len(n)) :  
    sum += int(n[i])**5

print(sum)

# 풀이 2
def five(n):
    num = list(map(int, list(n)))
    result = 0

    for n in num :
        result += n ** 5
    return result

print(five(input()))