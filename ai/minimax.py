from ai.heuristic import evaluate
from game.moves import generate_moves


def minimax(board, depth, alpha, beta, player):
    winner = board.check_winner()
    if depth == 0 or winner != 0:
        return evaluate(board, player), None

    moves = generate_moves(board, player)
    if not moves:
        return evaluate(board, player), None  # aucun coup possible

    best_move_result = None
    if player == 1:
        max_eval = -float('inf')
        for move in moves:
            b = board.clone()
            move(b)
            eval, _ = minimax(b, depth-1, alpha, beta, -player)
            if eval > max_eval:
                max_eval = eval
                best_move_result = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move_result
    else:
        min_eval = float('inf')
        for move in moves:
            b = board.clone()
            move(b)
            eval, _ = minimax(b, depth-1, alpha, beta, -player)
            if eval < min_eval:
                min_eval = eval
                best_move_result = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move_result



def best_move(board, depth, player):
    _, move = minimax(board, depth, -float('inf'), float('inf'), player)
    return move

