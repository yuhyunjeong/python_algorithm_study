a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    c = 0
    for i in s:
        if i == 'O':          
            c += 1
            sum += c
        else:
            c = 0
    print(sum)