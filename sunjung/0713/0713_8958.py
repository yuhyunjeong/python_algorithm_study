n = int(input())

for _ in range(n):
    a = input()
    score = 0
    sum = 0
    for i in a:
        if i == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)