for i in range(int(input())):
    result = [chr(i + 1) if i != 90 else 'A' for i in map(ord, input())]
    print(f"String #{i + 1}\n", *result, "\n", sep="")