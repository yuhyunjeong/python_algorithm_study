cnt = 0

for _ in range(int(input())):
    length, width, depth, weight = map(float, input().split())  

    allow = 0

    if (length <= 56 and width <= 45 and depth <= 25 and weight <= 7) or (length + width + depth <= 125 and weight <= 7) :
        allow = 1
        cnt += 1
    
    print(allow)

print(cnt)