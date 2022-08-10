# 풀이 1
result = 0
try:
    while True:
        if input():
            result += 1
except:
    print(result)

# 풀이 2
import sys

print(len(sys.stdin.readlines()))