def solution(X, Y):
    answer = ''

    # x_list = list(map(int,str(X)))
    # y_list = list(map(int,str(Y)))

    x_list = list(X)
    y_list = list(Y)

    # x_list = list(str(X))
    # y_list = list(str(Y))

    result = []

    for i in y_list: # 다중집합
        if i in x_list:
                x_list.remove(i)
                result.append(i)
                result.sort(reverse=True) # 내림차순
                answer = ' '.join(str(s) for s in result).replace(" ","") # 문자열 공백 없애기

        if answer=='':
            answer="-1"
        # elif answer.count("0") == len(answer): 
        elif int(answer) == 0:
            answer="0"
            
    
    return answer

print(solution(100,203045))