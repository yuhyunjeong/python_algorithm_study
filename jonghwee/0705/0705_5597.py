n = [i for i in range(1,31)]; #for 왼쪽에 있는 i는 오른쪽에서 만든 i를 집어넣는 것

for _ in range(28):
    report = int(input())
    n.remove(report)

print(min(n));
print(max(n));

#방법2 : set의 차집합 사용
result = [i for i in range(1, 31)]
sukje = []

while len(sukje) < 28:
    sukje.append(int(input()))
else:
    result = list(set(result).difference(sukje))
    print(min(result))
    print(max(result))