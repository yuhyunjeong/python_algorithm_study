def solution(want, number, discount):

    day = [0] * (len(discount) - 9)
    print(day)

    for i in range(len(discount) - 9):
        for j in range(len(want)):
            day[i] += min(discount[i:i + 10].count(want[j]), number[j])

    return day.count(10)

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))