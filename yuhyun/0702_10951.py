import sys



while True :
    try:
         test1, test2 = map(int, sys.stdin.readline().split()) 
         result = test1 + test2
         
        
    except:          # 예외가 발생했을때
        break

    else:            #예외가 발생하지 않았을때
        print(result)

"""
lines = sys.stdin.readlines() # readlines()는 입력값들을 list화..
for line in lines:
    num = list(map(int, line.split()))
    print(sum(num))           """