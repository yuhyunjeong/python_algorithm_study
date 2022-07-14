import sys

# input() 은 개행 문자 안들어감.
# sys.stdin.readline()는 개행문자가 들어감.
str = sys.stdin.readline().rstrip();

print(ord(str));