# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

n = int(input())

for i in range(n,0,-1) : # range(초기값, 마지막값, 증가값)
    print(i)