T = int(input())

for _ in range(T):
    
    n = int(input())
    winner = []
    win = ''
    for _ in range(n):
        one, two = input().split()
        if one == two:
            continue
        elif (one == 'R' and two == 'S') or (one == 'S' and two == 'P') or (one == 'P' and two == 'R'):
            winner.append('Player 1')
        else :
            winner.append('Player 2')
        
    if winner.count('Player 1') == winner.count('Player 2'):
        win = 'TIE'
    elif winner.count('Player 1') > winner.count('Player 2'):
        win = 'Player 1'
    else:
        win = 'Player 2'
    print(win)
        
        
