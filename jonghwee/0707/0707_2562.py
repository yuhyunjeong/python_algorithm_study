import sys

num_list=[];
for i in range(9):
    num_list.append(int(sys.stdin.readline().rstrip()))
print (max(num_list))
print(num_list.index(max(num_list))+1)

#풀이2
num = [int(input()) for _ in range(9)]
print(max(num))
print(num.index(max(num)) + 1)