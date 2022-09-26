class Board():

    def __init__(self):
        self.board = """"""
        self.positions = []
    

    def create_board(self):
        self.board = f"""
         1 2 3

      1  _|_|_
      2  _|_|_
      3   | | 

        
        """
        self.positions = self.create_positions()

        return self.board

    def create_positions(self):
        position = 0
        positions_list = []
        count = 1
        for char in self.board:
            if char == "|":
                if count%2 != 0 :
                    positions_list.append(position)
                count += 1
            position += 1
        self.positions = positions_list
        return self.positions

    def board_engine(self):
        pass


    def update_board(self, move_col, move_row, piece):
        list_of_moves = [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3)]
        checker = (move_col, move_row)
        if list_of_moves[0] == checker:
            self.board[self.positions[0]-1] = piece
        elif list_of_moves[0] == checker:
            self.board[self.positions[0]+1] = piece
        elif list_of_moves[0] == checker:
            self.board[self.positions[0]+3] = piece
        elif list_of_moves[1] == checker:
            self.board[self.positions[1]-1] = piece
        elif list_of_moves[1] == checker:
            self.board[self.positions[1]+1] = piece


