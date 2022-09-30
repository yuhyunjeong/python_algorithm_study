# 풀이 1: max() 함수 사용
n = input()
num = list(map(int, input().split()))
print(max(num))

# 풀이 2: for문 사용
n = input()
num = map(int, input().split())
result = 0
for i in num:
    if result < i:
        result = i
print(result)