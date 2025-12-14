class ConsoleUI:
    def display(self, board):
        symbols = {0:'□', 1:'○', -1:'●'}
        for i in range(0, 9, 3):
            print([symbols[board.state[j]] for j in range(i, i+3)])
        print()

    def ask_move(self, board):
        while True:
            try:
                i = int(input("Index 0-8 pour poser pion : "))
                if 0 <= i <= 8 and board.state[i] == 0:
                    break
                else:
                    print("Case invalide, essaye encore.")
            except ValueError:
                print("Entrez un nombre entre 0 et 8.")
        
        def move(b): 
            b.state[i] = 1  # toujours blanc pour le joueur humain
        return move
