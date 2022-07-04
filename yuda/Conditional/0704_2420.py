import math

num = list(map(int, input().split()))

result = num[0] - num[1]

if result >= 0:
    print(result)
else:
    print(result * -1)

# print(math.fabs(result))