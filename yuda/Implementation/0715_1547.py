import sys

cup = ['', 'O', 'X', 'X']

for _ in range(int(sys.stdin.readline())):
    change = list(map(int, sys.stdin.readline().split()))
    cup[change[0]], cup[change[1]] = cup[change[1]], cup[change[0]]

print(cup.index('O'))