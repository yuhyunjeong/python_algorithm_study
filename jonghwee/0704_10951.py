# while 1:
#     try:
#         A,B = map(int, input().split());
#         print(A+B);
#     except EOFError:
#         break;

import sys

lines = sys.stdin.readlines(); #readlines() 는 입력값들을 list로 만들어줌.
for line in lines:
    A,B=map(int,line.split());
    print(A+B);