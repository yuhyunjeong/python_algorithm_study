import sys


result = 0


while True :
    test1, test2 = map(int, sys.stdin.readline().split()) #테스트 케이스
    result = test1 + test2
    
    if test1 == 0 and test2 == 0 :
        break
    
    print(result)