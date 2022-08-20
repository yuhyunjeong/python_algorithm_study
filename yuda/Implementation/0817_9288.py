for i in range(int(input())):
    N = int(input())
    print(f"Case {i + 1}:")
    for j in range(1, 7):
        if 7 > N - j >= j:
            print(f"({j},{N - j})")