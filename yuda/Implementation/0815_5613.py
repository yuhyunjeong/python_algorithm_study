# 풀이 1
result = int(input())
while True:
    o = input()
    if o == "=":
        break
    if o == "+":
        result += int(input())
    elif o == "-":
        result -= int(input())
    elif o == "*":
        result *= int(input())
    else:
        result //= int(input())
print(result)

# 풀이 2
result = int(input())
while True:
    o = input()
    if o == "=":
        break
    result = eval(str(result) + o.replace("/", "//") + input())
print(result)