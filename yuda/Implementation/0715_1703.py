import sys

while True:
    tree = list(map(int, sys.stdin.readline().split()))

    if tree[0] == 0: break

    result = 1
    for i in range(tree[0]):
        result *= tree[1 + (i * 2)]
        result -= tree[2 + (i * 2)]
    print(result)