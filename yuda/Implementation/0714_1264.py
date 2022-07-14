import sys

M = ['a', 'e', 'i', 'o', 'u']

while True:
    line = list(sys.stdin.readline().rstrip().lower())
    if line[0] == '#':
        break
    
    result = 0
    for m in M:
        result += line.count(m)
    print(result)