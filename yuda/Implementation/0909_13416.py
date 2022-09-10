for _ in range(int(input())):
    result = 0
    for _ in range(int(input())):
        stock = list(map(int, input().split()))
        top = max(stock)
        if top > 0:
            result += top
    print(result)