class ConsoleUI:
    def display(self, board):
        symbols = {0:' ',1:'□',2:'□○',3:'□●',4:'○',5:'●'}
        for i in range(0,9,3):
            print([symbols[board.state[j]] for j in range(i,i+3)])
        print()


    def ask_move(self, board):
        i = int(input("Index 0-8 pour poser pion : "))
        def move(b): b.state[i] = 2
        return move