import sys

num = []
people = 0

for i in range(4):
    O , I = map(int, sys.stdin.readline().split())
     
    people -= O
    people += I

    num.append(people)

print(max(num))

