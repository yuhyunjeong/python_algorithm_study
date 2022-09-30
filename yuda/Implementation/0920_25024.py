last_date = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(int(input())):
    time = date = "No"
    x, y = map(int, input().split())
    if 0 <= x < 24 and 0 <= y < 60:
        time = "Yes"
        if 0 < x < 13 and 0 < y <= last_date[x]:
            date = "Yes"
    print(time, date)