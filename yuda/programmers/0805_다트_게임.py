def solution(dartResult):
    S = {"S":1, "D":2, "T":3}
    dartResult = dartResult.replace("10", "t")
    answer = []
    for i in dartResult:
        try:
            answer.append(int(i))
        except:
            if i == "t":
                answer.append(10)
            elif i in S.keys():
                answer[-1] **= S.get(i)
            elif i == "*":
                if len(answer) > 1:
                    answer[-2] *= 2
                answer[-1] *= 2
            else:
                answer[-1] *= -1
    return sum(answer)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))