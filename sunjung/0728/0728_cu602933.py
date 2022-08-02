#6029
""" a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n) """

#6030
""" n = ord(input()) #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
print(n) """

#6031
""" c = int(input())
print(chr(c)) #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 
              #chr( )는 정수값->문자, ord( )는 문자->정수값 """

#6032
""" n = int(input())
print(-n)  """#단항(unary) 연산자인 -(negative)를 변수 앞에 붙이면 부호가 반대인 값이 된다. 

#6033
n = ord(input()) #아스키코드 변환
print(chr(n+1)) #아스키 코드값에 1을 더해주어 다음 문자로 변환,  변환한 값을 chr() 유니코드 형태로 출력

