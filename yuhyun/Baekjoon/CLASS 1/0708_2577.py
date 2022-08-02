num = [int(input()) for _ in range(3)]
result = list(str(num[0] * num[1] * num[2]))

for i in range(10):
    print(result.count(str(i)))

# 풀이 2
multiple = 1
for _ in range(3):
    multiple *= int(input())

result = list(str(multiple))

for i in range(10):
    print(result.count(str(i)))

