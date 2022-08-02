import sys

# 6039
a,b = map(float,sys.stdin.readline().split());
print(a**b);

# 6040
a,b = map(int,sys.stdin.readline().split());
print(a//b);

# 6041
a,b = map(int,sys.stdin.readline().split());
print(a%b);

# 6042
a = float(sys.stdin.readline().rstrip());
print(format(a,".2f"));

# 6043
a,b = map(float,sys.stdin.readline().split());
print(format(a/b,".3f"));

# 6044
a,b = map(int,sys.stdin.readline().split());
print(a+b);
print(a-b);
print(a*b);
print(a//b);
print(a%b);
print(format(a/b,".2f"));

# 6045
a,b,c = map(int,sys.stdin.readline().split());
sum = a+b+c;
print(sum, format(sum/3,".2f"));

# 6046
a = int(sys.stdin.readline().rstrip());
print(a<<1);

# 6047
a,b = map(int,sys.stdin.readline().rstrip().split());
print(a<<b);

# 6048
a,b = map(int,sys.stdin.readline().rstrip().split());
print(a<b);

# 6049
a,b = map(int,sys.stdin.readline().rstrip().split());
print(a==b);

# 6050
a,b = map(int,sys.stdin.readline().rstrip().split());
print(a<=b);

# 6051
a,b = map(int,sys.stdin.readline().rstrip().split());
print(a!=b);

# 6052
a = int(sys.stdin.readline().rstrip());
print(bool(a));

# 6053
a = int(sys.stdin.readline().rstrip());
print(not(bool(a)));

# 6054
a,b = map(int,sys.stdin.readline().rstrip().split());
print(bool(a) and bool(b));

# 6055
a,b = map(int,sys.stdin.readline().rstrip().split());
print(bool(a) or bool(b));

# 6056
a,b = map(int,sys.stdin.readline().rstrip().split());
c = bool(a);
d = bool(b);
print((c and (not d)) or ((not c) and d));

# 6057
a,b = map(int,sys.stdin.readline().rstrip().split());
c = bool(a);
d = bool(b);
print((c and d) or ((not c) and (not d)));

# 6058
a,b = map(int,sys.stdin.readline().rstrip().split());
c = bool(a);
d = bool(b);
print((not c) and (not d));
print(not (a or b));