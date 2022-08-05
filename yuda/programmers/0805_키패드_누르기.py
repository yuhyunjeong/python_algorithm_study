def solution(numbers, hand):
    num = {1:[0, 0], 2:[0, 1], 3:[0, 2], 4:[1, 0], 5:[1, 1], 6:[1, 2], 7:[2, 0], 8:[2, 1], 9:[2, 2], "*":[3, 0], 0:[3, 1], "#":[3, 2]}
    left = num.get("*")
    right = num.get("#")
    answer = ''

    for n in numbers:
        i = num.get(n)
        if i[1] == 0:
            answer += 'L'
            left = i
        elif i[1] == 2:
            answer += 'R'
            right = i
        else:
            r_len = abs(i[0] - right[0]) + abs(i[1] - right[1])
            l_len = abs(i[0] - left[0]) + abs(i[1] - left[1])
            if r_len > l_len:
                answer += 'L'
                left = i
            elif r_len < l_len:
                answer += "R"
                right = i
            else:
                if hand == "left":
                    answer += "L"
                    left = i
                else:
                    answer += "R"
                    right = i
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))