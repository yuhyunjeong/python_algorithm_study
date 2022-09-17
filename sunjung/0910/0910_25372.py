#비밀번호는 6자리 이상 9자리 이하여야 한다.
n = int(input())
for _ in range (n):
    str = input()
    if len(str) >=6 and len(str) <=9 :
        print('yes')
    else :
        print('no')
