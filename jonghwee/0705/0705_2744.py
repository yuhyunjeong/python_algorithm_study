import sys


str = list(sys.stdin.readline().rstrip());

#풀이 1
#print(str.swapcase())

#풀이 2
for i in range(len(str)):
    if str[i].isupper():
        str[i] = str[i].lower();
    elif str[i].islower():
        str[i] = str[i].upper();
print("".join(i for i in str));
print(*str,sep="");
print(*str); #list 형태를 띄어쓰기 형태로 바꿔줌.