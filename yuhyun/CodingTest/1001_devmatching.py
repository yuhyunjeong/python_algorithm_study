# 1. - 3.1
import re

def solution(registered_list, new_id):
    answer = ''
    num = 0
    alphas = ''
 
       
    for i in registered_list:

        num = re.sub(r'[^a-z]', '', new_id)
        #num = re.findall('\d', new_id)
        alphas = re.findall('[a-z]', new_id)
        

        if i != new_id:
            answer = new_id
        
            
        if i == new_id:
            num += 1
            new_id = alphas+str(num)

    return answer

# 3. - 23.3
def solution(k):
    answer = 0

    lst = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    result = []

    for i in lst:

        if i == k :
            result.append(lst.index(i))
        
        for j in lst:

            if i + j == k:
                result.append((lst.index(i))*10 + lst.index(j))

            for l in lst:

                if i + j + l == k:
                    result.append((lst.index(i))*100 + lst.index(j)*10 + lst.index(l))

                for m in lst:

                    if i + j + l + m == k:
                        result.append((lst.index(i))*1000 + lst.index(j)*100 + lst.index(l)*10 + lst.index(m))


    answer = len(result)

    return answer

# 4. - 100
# SELECT P.ID, P.NAME, COUNT(*) AS "임대 가능일" FROM PLACES P JOIN SCHEDULES S ON P.ID = S.PLACE_ID GROUP BY P.ID, P.NAME
