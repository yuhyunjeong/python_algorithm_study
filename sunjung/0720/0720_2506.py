N = int(input())
score = list(map(int, input().split()))
sum = 0
result = 0

for i in range(N):

        if score[i] == 0 :
            sum = 0
        
        else:
            sum += 1
            result += sum

print(result)