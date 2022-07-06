import string


S = input()
#apb ='abcdefghijklmnopqrstuvwxyz'
apb = string.ascii_lowercase # 알파벳 소문자
# apb = list(range(97,123)) # a~z

for i in apb: # for문 in 문자열
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')
        