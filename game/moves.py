from itertools import product

def generate_moves(board, player):
    moves = []
    pawn = 4 if player == 1 else 5
    square_pawn = 2 if player == 1 else 3

    # Pose pion
    for i in range(9):
        if board.state[i] == 1:
            def m(b, i=i):
                b.state[i] = square_pawn
            moves.append(m)

    # Déplacement pion
    for i in range(9):
        if board.state[i] == pawn:
            for j in range(9):
                if board.state[j] == 1:
                    def m(b, i=i, j=j):
                        b.state[i] = 0
                        b.state[j] = pawn
                    moves.append(m)

    return moves
