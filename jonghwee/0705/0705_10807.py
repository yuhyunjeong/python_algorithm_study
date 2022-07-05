from itertools import count
import sys


N = int(sys.stdin.readline());
A = list(map(int,sys.stdin.readline().split()));
v = int(sys.stdin.readline());

print(A.count(v));
