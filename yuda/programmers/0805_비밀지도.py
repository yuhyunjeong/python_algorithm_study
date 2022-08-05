# 풀이 1
def solution(n, arr1, arr2):
    answer = [""] * n
    for i in range(n):
        for j in range(n):
            if arr1[i] % (2 ** (n - j)) // 2 ** (n - j - 1) == 1 or arr2[i] % (2 ** (n - j)) // 2 ** (n - j - 1) == 1:
                answer[i] += "#"
            else:
                answer[i] += " "
    return answer

# 풀이 2
def solution2(n, arr1, arr2):
    answer = [""] * n
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if arr1[i] // (2 ** j) == 1 or arr2[i] // (2 ** j) == 1:
                answer[i] += "#"
            else:
                answer[i] += " "
            arr1[i] %= 2 ** j
            arr2[i] %= 2 ** j
    return answer

print(solution2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution2(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))