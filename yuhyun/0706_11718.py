
import sys

# 풀이 1
while True :
    try :
        str = input() # input -> 하나씩 실행
        print(str)
    except EOFError: # 런타임에러
        break

# 풀이 2
str = sys.stdin.readlines() # 모든 입력값이 한 줄에 들어감. 런타임 에러 X

for line in str :
    print(line.rstrip()) # 개행문자 없앰