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

# from re import I


# def solution(garden):
#     answer = 0
#     cnt = 0

#     for i in range(len(garden)):
#         for j in range(len(garden[i])):
            
#             if garden.count(1) == len(garden)*len(garden[i]):
#                 break

#             if garden[i][j] == 1:
#                 garden[i] = 1
#                 garden[][j] = 1
                
#                 answer += 1
  
#     return answer

# print(solution([[0,0,0],[0,1,0],[0,0,0]]))