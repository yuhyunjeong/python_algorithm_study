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