for i in range(int(input())):
    tri = sorted(list(map(int, input().split())))
    if tri[2] >= tri[0] + tri[1]:
        result = "invalid!"
    elif tri[0] == tri[1] == tri[2]:
        result = "equilateral"
    elif tri[0] == tri[1] or tri[1] == tri[2]:
        result = "isosceles"
    else:
        result = "scalene"
    print(f"Case #{i + 1}: {result}")