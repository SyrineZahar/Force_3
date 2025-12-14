def evaluate(board, player):
    winner = board.check_winner()
    if winner == player:
        return 1000
    if winner == -player:
        return -1000


    score = 0
    center = board.state[4]
    if (player == 1 and center in (2,4)) or (player == -1 and center in (3,5)):
        score += 5


    score += len([c for c in board.state if c in (2,4)]) * 3
    score -= len([c for c in board.state if c in (3,5)]) * 3


    return score