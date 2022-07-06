import sys

T = int(sys.stdin.readline().rstrip());
answer=[]
for i in range(T):
    str = sys.stdin.readline().rstrip();
    answer.append(str);
for i in answer:
    print(i[0], end="")
    print(i[len(i)-1])

#풀이 2
for _ in range(T) :
    str= input()
    print(str[0:1],str[-1],sep="");