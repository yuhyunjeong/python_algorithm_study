import sys

list = []

for i in range(7) : #7개 입력
    a = int(input())
    if a % 2 != 0 : #홀수라면
        list.append(a) #배열에 추가

if list: #list가 존재한다면
    print(sum(list))
    print(min(list))
else:   #list가 존재하지 않는다면
    print(-1)
