T = int(input())
 
for _ in range(T):
    n = bin(int(input()))[2:] #bin 함수를 이용하여 10진수 형태의 입력을 2진수 형태로 변경한다. bin함수로 변환하게되면 ob1010과 같은 값이 나오는데 숫자만 사용하기 위해 슬라이싱으로 [2:] 잘라준다.
    for i in range(len(n)):
        if n[-i - 1] == '1':
            print(i, end=' ')
