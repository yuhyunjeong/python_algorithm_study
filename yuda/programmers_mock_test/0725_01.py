def solution(X, Y):
    X = list(X)
    Y = list(Y)

    G = set(X).intersection(Y)
    if G == set():
        return '-1'

    answer = ''
    for i in sorted(list(G), reverse=True):
        answer += i * min(X.count(i), Y.count(i))

    return str(int(answer))

print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))
print(solution("1935487", "2754682"))