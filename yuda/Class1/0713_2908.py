import sys

num = sys.stdin.readline().split()

for i in range(2):
    num[i] = num[i][::-1]

print(num[0] if num[0] > num[1] else num[1])