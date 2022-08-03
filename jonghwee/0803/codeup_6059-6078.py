import sys

# 6059
a = int(sys.stdin.readline().rstrip());
print(~a);

# 6060
a,b = map(int,sys.stdin.readline().split());
print(a&b);

# 6061
a,b = map(int,sys.stdin.readline().split());
print(a|b);

# 6062
a,b = map(int,sys.stdin.readline().split());
print(a^b);

# 6063
a,b = map(int,sys.stdin.readline().split());
print(int(a if (a>=b) else b));

# 6064
a,b,c = map(int,sys.stdin.readline().split());
print(int((a if (a<=b) else b) if((a if (a<=b) else b)<c) else c));

# 6065
a,b,c = map(int,sys.stdin.readline().split());
if a%2==0:
    print(a);
if b%2==0:
    print(b);
if c%2==0:
    print(c);

# 6066
a,b,c = map(int,sys.stdin.readline().split());
if a%2==0:
    print("even");
else:
    print("odd");
if b%2==0:
    print("even");
else:
    print("odd");
if c%2==0:
    print("even");
else:
    print("odd");

# 6067
a = int(sys.stdin.readline().rstrip());
if a<0:
    if a%2==0:
        print("A");
    else:
        print("B");
else:
    if a%2==0:
        print("C");
    else:
        print("D");

# 6068
a = int(sys.stdin.readline().rstrip());
if a>=90:
    print("A");
else:
    if a>=70:
        print("B");
    else:
        if a>=40:
            print("C");
        else:
            print("D");

# 6069
str = sys.stdin.readline().rstrip();
if str=="A":
    print("best!!!");
else:
    if str=="B":
        print("good!!");
    else:
        if str=="C":
            print("run!");
        else:
            if str=="D":
                print("slowly~");
            else:
                print("what?");

# 6070
month = int(sys.stdin.readline().rstrip());
q = month//3;

if q==1:
    print("spring");
else:
    if q==2:
        print("summer");
    else:
        if q==3:
            print("fall");
        else:
            print("winter");

# 6071
a=1;
while a!=0:
    a = int(sys.stdin.readline().rstrip());
    if a!=0:
        print(a);
    else:
        break;

# 6072
a=int(sys.stdin.readline().rstrip());
while a!=0:
    print(a);
    a = a-1;

# 6073
a=int(sys.stdin.readline().rstrip());
while a>=0:
    if a!=0:
        print(a-1);
        a = a-1;
    else:
        break;

# 6074
a = ord(sys.stdin.readline().rstrip());
b = ord("a");
while b<=a:
    print(chr(b), end=" ");
    b += 1;

# 6075
a = int(sys.stdin.readline().rstrip());
b = 0;
while b<=a:
    print (b, end=" ");
    b += 1;

# 6076
a = int(sys.stdin.readline().rstrip());
for i in range(0,a+1):
    print(i);

# 6077 - 풀이 1
a=int(sys.stdin.readline().rstrip());
sum=0;

for i in range(1,a+1):
    if i%2==0:
        sum += i;
print(sum);

# 6077 - 풀이 2
a=int(sys.stdin.readline().rstrip());
b=0;
sum=0;

while b<a:
    b+=1;
    if b%2==0:
        sum+=b;
print(sum)

# 6078
a="a";
while a!="q":
    a = sys.stdin.readline().rstrip();
    print(a);