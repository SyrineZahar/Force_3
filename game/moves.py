from itertools import product

def generate_moves(board, player):
    moves = []

    # Pose pion
    for i in range(9):
        if board.state[i] == 0:
            def m(b, i=i):
                b.state[i] = player
            moves.append(m)

    # Déplacement pion (optionnel si ton jeu le permet)
    # ici on peut ajouter un déplacement d’un pion existant vers une case vide

    return moves
