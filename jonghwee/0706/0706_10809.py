import string
import sys

letter = sys.stdin.readline();
abc = string.ascii_lowercase;
# print(abc)
# for i in range(0,len(abc)):
#     for j in range(0,len(letter)):
#         if abc[i]==letter[j]:
#             print(i)
#         else:
#             print(-1)

#풀이 1
for i in abc:
    print(letter.find(i));

#풀이 2
abc_list = list(string.ascii_lowercase);
num_list=[];

for i in range(len(abc_list)):
    if abc_list[i] in letter:
        num_list.append(str(letter.index(abc_list[i])))
    else:
        num_list.append('-1')
print(num_list)
print (' '.join(num_list));
print(*num_list);