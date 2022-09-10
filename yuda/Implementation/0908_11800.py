num = {1:"Yakk", 2:"Doh", 3:"Seh", 4:"Ghar", 5:"Bang", 6:"Sheesh"}
same = {1:"Habb Yakk", 2:"Dobara", 3:"Dousa", 4:"Dorgy", 5:"Dabash", 6:"Dosh"}

for i in range(int(input())):
    a, b = sorted(map(int, input().split()))
    print(f"Case {i + 1}: ", end="")
    if a == b:
        print(same[a])
    elif a + b == 11:
        print("Sheesh Beesh")
    else:
        print(num[b], num[a])