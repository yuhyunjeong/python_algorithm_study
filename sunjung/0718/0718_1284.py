while True:
    n = input()
    if n == '0': #0은 처리하지 않는다
        break
    result =  2 + int(len(n)) - 1 #양옆 공백 + (숫자의 길이 - 1 = 사이 공백 수)

    for i in n:
        if i == '0': #1은 2cm, 2~나머지는 3cm, 0은 4cm를 차지
           result += 4 
        elif i == '1':
           result += 2
        else:
           result += 3
    print(result)