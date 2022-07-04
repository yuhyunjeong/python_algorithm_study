import sys



while True :
    try:
         test1, test2 = map(int, sys.stdin.readline().split()) 
         result = test1 + test2
        
    except:          # 예외가 발생했을때
        break
    else:            #예외가 발생하지 않았을때
        print(result)
    