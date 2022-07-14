import sys

word = list(sys.stdin.readline().rstrip().upper())
check = list(set(word))
result = []

for i in check:
    result.append(word.count(i))

if result.count(max(result)) > 1:
    print("?")
else:
    print(check[result.index(max(result))])