# 풀이 1
def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        doll = 0
        for j in range(len(board)):
            doll = board[j][i - 1]
            if doll != 0:
                board[j][i - 1] = 0
                break
        if doll == 0:
            continue
        if len(box) == 0:
            box.append(doll)
            continue
        if doll == box[-1]:
            box.pop()
            answer += 2
        else:
            box.append(doll)
    return answer

# 풀이 2
def solution(board, moves):
    answer = 0
    box = []
    for i in moves:
        for j in range(len(board)):
            doll = board[j][i - 1]
            if doll != 0:
                board[j][i - 1] = 0
                if len(box) > 0 and doll == box[-1]:
                    box.pop()
                    answer += 2
                else:
                    box.append(doll)
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))