from game.board import Board
from ui.console import ConsoleUI
from ai.minimax import best_move


board = Board()
ui = ConsoleUI()


current_player = 1 # 1 = blanc, -1 = noir


while True:
    ui.display(board)


    if board.check_winner() != 0:
        print("Victoire du joueur", "Blanc" if board.check_winner() == 1 else "Noir")
        break


    if current_player == 1:
        move = ui.ask_move(board)
    else:
        move = best_move(board, depth=3, player=current_player)


    board.apply_move(move)
    current_player *= -1