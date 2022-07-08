# 첫째 줄에 다섯 자리인 양의 정수 n이 주어진다.
# 각 자릿수의 다섯제곱의 합을 출력

n = int(input())
sum = 0

for i in range(len(n)) :
    sum += int(n[i])**5

print(sum)
