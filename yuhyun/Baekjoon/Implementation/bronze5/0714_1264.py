import sys


while True :
    str = sys.stdin.readline().rstrip()
    cnt = 0

    if str == "#" :
        break
    
    for i in str :       
        if i.lower() in ['a','e','i','o','u']:
            cnt += 1
    print(cnt)

   


    