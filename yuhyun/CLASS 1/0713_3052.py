arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)
arr = set(arr)  # set : 중복 제거
print(len(arr)) # list 길이 구하기

# 풀이 2

import sys

result = set()

for _ in range(10):
    result.add(int(sys.stdin.readline()) % 42)

print(len(result))




