# Python3 로 제출하면 시간초과 -> pypy3 으로 제출

n = int(input())

def fib(n) :
    if n == 1 or n == 2:
        return 1  # 코드1

    else:
        return (fib(n - 1) + fib(n - 2))


def fibonacci(n) :
    f = [0]*(n+1)
    f[1] , f[2] = 1,1
    cnt = 0

    for i in range(3 , n+1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]  # 코드2
    return cnt

# fibonacci(n) {
#     f[1] <- f[2] <- 1;
#     for i <- 3 to n
#         f[i] <- f[i - 1] + f[i - 2];  # 코드2
#     return f[n];
# }

print(fib(n),fibonacci(n))

# 풀이 2

n = int(input())
ans = [0, 1]
dp_li = [0, 1, 1]

def recur(n):
    global ans
    if n < 3:
        ans[0] += 1
        return 1
    else: return recur(n - 1) + recur(n - 2)

def dp(n):
    global ans, dp_li
    if n < 3: return dp_li[n]
    for i in range(3, n):
        ans[1] += 1
        dp_li.append(dp_li[i - 1] + dp_li[i - 2])
    return dp_li[-1]

recur(n)
dp(n)
print(*ans)