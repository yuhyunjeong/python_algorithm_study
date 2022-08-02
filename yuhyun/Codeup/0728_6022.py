s=input()

a=0
for i in range(len(s)):  
    print(s[a:a+2],end=' ')
    a+=2

# 풀이 2
a = input()

for i in range(0, len(a)-1,2):
    print(a[i:i+2], end=" ")