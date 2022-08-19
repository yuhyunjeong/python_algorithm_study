def solution(name_list):
    answer = 0
    for name in name_list:
        for n in name:
            if n == 'j' or n == 'k':
                answer += 1
                '''
                이름에 들어가는 j와 k를 모두 찾는 게 아니라 j와 k가 하나라도 들어가는 사람을 찾는 것
                continue를 사용할 경우 한 사람의 이름 안에서 j와 k가 존재할 때마다 += 1 하기 때문에 break로 변경
                '''
                break
    return answer