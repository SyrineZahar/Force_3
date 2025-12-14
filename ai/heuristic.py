def evaluate(board, player):
    winner = board.check_winner()
    if winner == player:
        return 1000
    if winner == -player:
        return -1000

    score = 0
    lines = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    
    for a,b,c in lines:
        line = [board.state[a], board.state[b], board.state[c]]
        # victoire immédiate
        if line.count(player) == 2 and line.count(0) == 1:
            score += 100
        # blocage adversaire
        if line.count(-player) == 2 and line.count(0) == 1:
            score += 80
        # avantages généraux
        score += line.count(player) * 10
        score -= line.count(-player) * 10

    return score
