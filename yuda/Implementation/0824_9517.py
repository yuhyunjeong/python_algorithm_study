# for문
K = int(input())
N = int(input())
time = 0
for i in range(N):
    T, Z = input().split()
    time += int(T)
    if time >= 210:
        print(K)
        break
    if Z == 'T':
        K = K % 8 + 1

# while문
K = int(input())
N = int(input())
time = 0
while time < 210:
    T, Z = input().split()
    time += int(T)
    if time >= 210:
        print(K)
    if Z == 'T':
        K = K % 8 + 1