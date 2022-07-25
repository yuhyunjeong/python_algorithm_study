import sys


T = int(input())

for _ in range(T) :
    R, S = sys.stdin.readline().rstrip().split()
    str=""
    for i in S :
        str += i*int(R)
    print(str)
