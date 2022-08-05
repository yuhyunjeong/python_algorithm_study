# A<B<C
num = list(map(int, input().split(' ')))
alph = input()
num = sorted(num) #sorted(리스트) 는 본체 리스트는 내버려두고, 정렬한 새로운 리스트를 반환

for i in alph :
    if i == 'A':
        print(num[0], end =' ')
    elif i == 'B':
        print(num[1], end =' ')
    elif i == 'C':
        print(num[2], end =' ')


#2
N = sorted(list(map(int, input().split())))
S = list(input())

for i in range(3):
    S[S.index(chr(65 + i))] = N[i]

print(*S)