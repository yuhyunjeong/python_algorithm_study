""" 
a 300초
b 60초
c 10초 
"""

t = input()

if(t %10 != 0) : #1의 자리가 0이 아니면 -1을 출력
    print(-1)


#두번째 풀이
n = int(input())
if n % 10:
    print(-1)
else:
    print(n // 300, n % 300 // 60, n % 60 // 10)
    