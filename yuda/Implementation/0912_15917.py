import sys
for _ in range(int(sys.stdin.readline())):
    n = str(bin(int(sys.stdin.readline()))[3:])
    if n.count("1"):
        print(0)
    else:
        print(1)