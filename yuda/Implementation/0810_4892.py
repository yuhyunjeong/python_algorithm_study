i = 1
while True:
    n = int(input())
    if not n:
        break
    print(f"{i}. odd {n // 2}" if n % 2 else f"{i}. even {n // 2}")
    i += 1