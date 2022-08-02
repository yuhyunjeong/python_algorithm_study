import sys


num = int(sys.stdin.readline()) #개수 

result = 0

for i in range(num) :
    test1, test2 = map(int, sys.stdin.readline().split()) #테스트 케이스
    result = test1 + test2
    print(result)