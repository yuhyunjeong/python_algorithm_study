arr = [list(map(int, input().split())) for _ in range(9)]

#print(max(arr)) # 해당 배열에서 원소값의 합이 최대인 행을 출력

num = max(map(max,arr))
ind = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == num:
            #ind.append([i,j])
            ind.extend([i+1,j+1]) # 두개의 리스트를 합침
            result = ' '.join(str(s) for s in ind)

print(num)
print(result)


