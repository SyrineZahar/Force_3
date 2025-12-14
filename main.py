from game.board import Board
from ui.console import ConsoleUI
from ai.minimax import best_move

board = Board()
ui = ConsoleUI()

current_player = 1  # 1 = joueur humain (blanc), -1 = IA (noir)

while True:
    ui.display(board)

    if current_player == 1:
        move = ui.ask_move(board)
    else:
        move = best_move(board, depth=5, player=current_player)  # current_player doit être défini avant

    board.apply_move(move)

    # Vérifier victoire
    winner = board.check_winner()
    if winner != 0:
        ui.display(board)
        print("Victoire du joueur", "Blanc" if winner == 1 else "Noir")
        break

    current_player *= -1
