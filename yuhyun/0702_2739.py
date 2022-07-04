import sys


num = int(sys.stdin.readline())


for i in range(9) :
    i += 1
    result = num * i
    print(num,'*',i,'=', result) # , 사용하면 한칸씩 띄어 출력됨
    