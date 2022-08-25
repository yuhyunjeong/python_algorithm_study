def solution(garden):
    answer = 0
    X = [0, 1, 0, -1]
    Y = [1, 0, -1, 0]
    flower = []
    n = len(garden)
    m = len(garden[0])
    while True:
        for i in range(n):
            for j in range(m):
                if garden[i][j]:
                    flower.append([i, j])
        for f in flower:
            for x, y in zip(X, Y):
                i = f[0] + x
                j = f[1] + y
                if  0 <= i < n and 0 <= j < m:
                    garden[i][j] = 1
        if len(flower) != n * m:
            answer += 1
            flower = []
        else:
            break
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")