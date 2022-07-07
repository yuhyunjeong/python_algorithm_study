#첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

num = []
for _ in range(9):
    i = int(input())
    num.append(i)
    
print(max(num))
print(num.index(max(num))+1) #index는 0부터 시작, 1을 더해준다