num = list(map(int, input().split()))
odd = [i for i in num if i % 2]
result = 1
if len(odd):
    for o in odd:
        result *= o
else:
    for n in num:
        result *= n
print(result)