#N개의 숫자를 공백 없이 입력, 입력받은 숫자를 모두 합해서 출력
n = input()
print(sum(map(int,input())))

# 풀이2
N = int(input())
num = input()
result = 0

for i in range(N) :
    result += int(num[i])
    
print(result)
