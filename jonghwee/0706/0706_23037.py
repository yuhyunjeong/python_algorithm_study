import sys

n = int(sys.stdin.readline());
letter = str(n);
list=[]

for i in range(len(letter)):
    list.append(int(letter[i])**5)
print(sum(list))

#풀이2 - 함수 사용
def five(n):
    num=list(map(int,list(n)))
    result = 0

    for n in num:
        return result;
print(five(input()))