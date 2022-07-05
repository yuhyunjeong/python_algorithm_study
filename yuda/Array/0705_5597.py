# while문 사용
result = [i for i in range(1, 31)]

while len(result) > 2:
    result.remove(int(input()))

print(min(result))
print(max(result))

# set의 차집합 사용
result = [i for i in range(1, 31)]
sukje = []

while len(sukje) < 28:
    sukje.append(int(input()))
else:
    result = list(set(result).difference(sukje))
    print(min(result))
    print(max(result))