# 풀이 1
def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = list(set(report))

    count = {}
    for R in report:
        R = list(R.split())
        if R[1] in count:
            count[R[1]] += [R[0]]
        else:
            count[R[1]] = [R[0]]

    for id in id_list:
        if id in count:
            if len(count[id]) >= k:
                for count_id in count[id]:
                    answer[id_list.index(count_id)] += 1
    return answer

# 풀이 2
def solution2(id_list, report, k):
    answer = [0] * len(id_list)

    reports = {id : 0 for id in id_list}

    for R in set(report):
        R = list(R.split())
        reports[R[1]] += 1

    for R in set(report):
        R = list(R.split())
        if reports[R[1]] >= k:
            answer[id_list.index(R[0])] += 1
    return answer