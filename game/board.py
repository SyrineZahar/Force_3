import copy


class Board:
    def __init__(self):
        self.state = [0]*9  
        self.last_move = None


    def clone(self):
     return copy.deepcopy(self)


    def apply_move(self, move):
     move(self)


    def get_cells(self, value):
        return [i for i, v in enumerate(self.state) if v == value]


    def check_winner(self):
        lines = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        for a, b, c in lines:
            if self.state[a] != 0 and self.state[a] == self.state[b] == self.state[c]:
                return self.state[a]  # renvoie 1 (blanc) ou -1 (noir)
        return 0  # pas de gagnant
