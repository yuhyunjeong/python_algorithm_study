vote = [input() for _ in range(int(input()))]
print("Junhee is cute!" if vote.count("1") > vote.count("0") else "Junhee is not cute!")