
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

    def place_chip(self, position, player):
        if position == "r1_1" and player == 1:
            self.board = """
                1 2 3

            1  X|_|_
            2  _|_|_
            3   | |

                
                """
        elif position == "r1_1" and player == 2:
            self.board

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
        return positions_list

