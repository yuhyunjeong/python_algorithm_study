num = int(input())

result = 1
for i in range(1, num + 1):
    result *= i
print(result)

# def fact(num):
#     if num ==0:
#         return 1
#     a = num * fact(num-1)  
#     print(a)
#     return a

# N = int(input())
# print(fact(N))