# 풀이 1
for _ in range(int(input())):
    n = int(input())
    result = []
    B = int(n ** 0.5)
    while n != 0:
        if n - (2 ** B) >= 0:
            result.insert(0, B)
            n -= 2 ** B
        B -= 1
    print(*result)

# 풀이 2
for _ in range(int(input())):
    n = list(bin(int(input()))[2:])
    n.reverse()
    for i in range(len(n)):
        if n[i] == "1":
            print(i, end=" ")

# 풀이 3
for _ in range(int(input())):
    n = bin(int(input()))[2:]
    for i in range(1, len(n) + 1):
        if n[-i] == "1":
            print(i - 1, end=" ")

# 풀이 4
for _ in range(int(input())):
    n = bin(int(input()))[2:][::-1]
    print(*[i for i in range(len(n)) if n[i] == "1"])