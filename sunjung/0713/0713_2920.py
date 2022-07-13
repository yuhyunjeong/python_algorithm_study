#첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

num = list(map(int, input().split()))

if num == sorted(num) :
    print('ascending')
elif num == sorted(num, reverse=True):
    print('descending')
else:
    print('mixed')

