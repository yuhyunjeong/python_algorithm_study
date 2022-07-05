# for문 사용
N = int(input())
num = list(map(int, input().split()))
v = int(input())
result = 0

for i in num:
    if i == v:
        result += 1

print(result)

# count() 함수 사용
N = int(input())
num = list(map(int, input().split()))
v = int(input())

print(num.count(v))