while 1:
    n = input()
    
    if n == '0':
        break

    while len(n) > 1:
        result = 0
        
        for i in n:
            
            result = result + int(i)
            
        n = str(result)

    print(int(n))