n = input()

def fibo(a) :
    if a <= 1:
        return a # 무한반복 방지
    return fibo(a-1)+fibo(a-2)

print(fibo(int(n)))