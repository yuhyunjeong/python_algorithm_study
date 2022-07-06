def five(n):
    num = list(map(int, list(n)))
    result = 0

    for n in num:
        result += n ** 5

    return result

print(five(input()))