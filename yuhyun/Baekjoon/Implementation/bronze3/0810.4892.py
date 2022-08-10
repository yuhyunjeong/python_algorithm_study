cnt = 1
while True:

    n_zero = int(input())
    
    if n_zero == 0 :
        break

    n_fi = 3*(n_zero)

    if n_fi % 2 == 0:
        n_tw = n_fi / 2
    else:
        n_tw = (n_fi + 1) / 2

    n_th = 3*(n_tw)

    n_fo = int(n_th / 9)
    
    
    if n_fi % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    
    print(f"{cnt}. {result} {n_fo}")
    cnt += 1

    
# 풀이 2

# i = 1
# while True:
#     n = int(input())
#     if not n:
#         break
#     print(f"{i}. odd {n // 2}" if n % 2 else f"{i}. even {n // 2}")
#     i += 1
