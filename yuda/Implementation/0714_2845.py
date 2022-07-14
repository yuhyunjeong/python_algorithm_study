num = list(map(int, input().split()))
people = list(map(int, input().split()))
result = [i - num[0] * num[1] for i in people]
print(*result)