lst = list(map(int, input().split()))
result = "mixed"

if lst == sorted(lst):
    result = "ascending"
elif lst == sorted(lst, reverse=True):
    result = "descending"

print(result)