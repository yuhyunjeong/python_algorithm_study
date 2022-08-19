from sys import stdin

for _ in range(int(input())):
    a,b = map(int, stdin.readline().split())
    print(f"Case {_+1}: {a+b}")
