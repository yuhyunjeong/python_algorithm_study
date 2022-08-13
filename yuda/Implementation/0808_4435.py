G = {0:1, 1:2, 2:3, 3:3, 4:4, 5:10}
S = {0:1, 1:2, 2:2, 3:2, 4:3, 5:5, 6:10}

for i in range(int(input())):
    gan = list(map(int, input().split()))
    sa = list(map(int, input().split()))

    for j in range(len(sa)):
        if j < len(gan):
            gan[j] *= G[j]
        sa[j] *= S[j]

    print("Battle %d: " % (i + 1), end="")
    if sum(gan) > sum(sa):
        print("Good triumphs over Evil")
    elif sum(gan) < sum(sa):
        print("Evil eradicates all trace of Good")
    else:
        print("No victor on this battle field")