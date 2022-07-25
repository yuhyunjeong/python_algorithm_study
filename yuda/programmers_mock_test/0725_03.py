def solution(order):
    answer = 0
    main_stack = [i for i in range(1, len(order) + 1)]
    sub_stack = []
    while True:
        if len(sub_stack) > 0 and sub_stack[-1] == order[0]:
            del sub_stack[-1]
            del order[0]
            answer += 1
        elif len(main_stack) > 0:
            if main_stack[0] == order[0]:
                del main_stack[0]
                del order[0]
                answer += 1
            elif main_stack.count(order[0]) == 1:
                sub_stack.extend(main_stack[0:main_stack.index(order[0])])
                del main_stack[0:main_stack.index(order[0])]
            else:
                break
        else:
            break
    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))