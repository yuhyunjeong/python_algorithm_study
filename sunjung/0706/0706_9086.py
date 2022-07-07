# 입력의 첫 줄에는 테스트 케이스의 개수 
# 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력

i = int(input())

for j in range(i):
    w = str(input())
    print(w[0]+w[-1])

#---------------------

T = int(input())

for _ in range(T) :
    str = input()
    print(str[0:1],str[-1],sep="") #문자열 인덱싱
