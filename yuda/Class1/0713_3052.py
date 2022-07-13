import sys

result = set()

for _ in range(10):
    result.add(int(sys.stdin.readline()) % 42)

print(len(result))