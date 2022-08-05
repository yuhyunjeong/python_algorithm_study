import re


def solution(new_id):
    answer = ''

    new_id = new_id.lower() # 알파벳 소문자
    
    answer = re.sub(r'[^a-z0-9-_.]','',new_id) #알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거

    # 3
    while '..' in answer:
        answer = answer.replace('..', '.') 
        
    # 4
    if answer[0] == '.': # answer.startswith('.')
        if len(answer) >= 2:
            answer = answer[1:]
    
    if answer[-1] == '.': # answer.endswith('.')
        answer = answer[:-1]
        
    # 5
    if answer == '':
        answer = 'a'
        
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
            
    # 7
    while len(answer) < 3:
        answer += answer[-1]


    return answer