for _ in range(int(input())) : #0b1101
    n = bin(int(input()))[2:] #1101
    for i in range (len(n)):
        if n[-i - 1] == '1' : #이진수의 값 역순 [-i-1]
            print(i, end=' ')
    

