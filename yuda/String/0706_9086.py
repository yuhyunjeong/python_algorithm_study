import sys

for i in range(int(input())):
    str = sys.stdin.readline().rstrip()
    print(str[0], str[-1], sep="")