# 세개의 자연수 ABC, 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 
# 차례로 한 줄에 하나씩 출력한다.

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C)) #string으로 변환해야 잘려서 출력된다!
for i in range(10): #1부터 9까지의 숫자가 각각 몇 번 쓰였는지 출력
    print(result.count(str(i)))

#풀이2
num = [int(input()) for _ in range(3)]
N = list(str(num[0] * num[1] * num[2]))

for i in range(10):
    print(N.count(str(i)))

#풀이3
multiple = 1
for _ in range(3) :
    multiple *= int(input())

N = list(str(multiple))

for i in range(10):
    print(N.count(str(i)))