import sys

x = int(sys.stdin.readline());
y = int(sys.stdin.readline());

if(x>0 and y>0) : print(1);
elif(x>0 and y<0) : print(4);
elif(x<0 and y<0) : print(3);
elif(x<0 and y>0) : print(2);

# and 대신에 | 써도 값은 나옴. 무슨 차이인지