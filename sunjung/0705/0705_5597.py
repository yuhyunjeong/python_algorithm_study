import sys

student = [i for i in range(1,31)]
for _ in range(28) :
    student.remove(int(input()))

print('출력---')
print(*student,sep="\n") #배열 앞에 * 연산자를 붙여서 출력 가능
#print(student,sep="\n")

#------------------------------------

result = [i for i in range(1, 31)]
sukje = []

while len(sukje) < 28:
    sukje.append(int(input()))
else:
    result = list(set(result).difference(sukje))
    print(min(result))
    print(max(result))