# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

n = int(input())
num = list(map(int,input().split()))
v = int(input())

print(num.count(v))