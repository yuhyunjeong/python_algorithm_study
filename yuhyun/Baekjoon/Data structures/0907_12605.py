n = int(input())

for i in range(n):
    str = list(input().split())
    str.reverse()

    print(f"Case #{i+1}:",*str)