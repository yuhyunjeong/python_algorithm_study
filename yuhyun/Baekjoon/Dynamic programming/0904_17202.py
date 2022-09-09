A = list(map(int, input()))
B = list(map(int, input()))
arr = [0]*16
for i in range(16):
    if i % 2 == 0:
        arr[i] = A[i//2]  # 0,2,4 ...
    else:
        arr[i] = B[i//2] # 1,3,5 ...

#print(arr)

while len(arr) != 2:
    temp = []
    for i in range(len(arr)-1): # 0+1 ~ 15+16
        num = (arr[i]+arr[i+1]) % 10 # 1의자리수
        temp.append(num)
    arr = temp

print(*arr, sep="")
