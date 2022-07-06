# 첫째 줄에 다섯 자리인 양의 정수 n이 주어진다.
# 각 자릿수의 다섯제곱의 합을 출력

n = int(input())

result = 0
for i in range(n) :
    result += int(i)**5

print(result)
