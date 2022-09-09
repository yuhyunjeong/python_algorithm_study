import sys
k, l = sys.stdin.readline().split()

for i in range(2,int(l)): # l 보다 작은 인수를 찾는 것이므로 2 ~ l 까지만 비교하면 된다
    if(int(k) % i == 0):
        print("BAD", i)
        exit()
        
print("GOOD")


# 시간초과
# k, l = map(int, input().split())

# for i in range(2, k):

#     if k % i == 0:

#         if i >= l:
#             result = True
#         else:
#             result = False
#             print(f"BAD {i}")
#             exit()

# if result == True:
#     print('GOOD')
    