import pandas as pd

class GamePlay():

    def __init__(self, player_name, other_name):
        self.player_1 = player_name
        self.player_2 = other_name
        self.moves = {
            self.player_1: [],
            self.player_2: []
            }
        self.game_instructions = """
        INSTRUCTIONS:

        The board looks like this 
        
         1 2 3

      1  _|_|_
      2  _|_|_
      3   | | 
        
        To make a move you must choose column and row, choosing (1,1) for example would put a move as shown below:

         1 2 3

      1  X|_|_
      2  _|_|_
      3   | | 

----------------------------------------------------------------------------------------------------------------------------------------
        """
        self.winner = ""



    def ask_move(self, user_player):
        move_output_col = input(f"[{user_player}] Please provide a Column: ")
        move_output_row = input(f"[{user_player}] Please provide a Row: ")
        if move_output_col.isdigit() and move_output_row.isdigit():
            if 1 <= int(move_output_col) <= 3 and 1 <= int(move_output_row) <= 3:
                self.check_move(move=(int(move_output_col), int(move_output_row)), user_player=user_player)
                check_valid = self.check_move((int(move_output_col), int(move_output_row)), user_player)
                print(check_valid)
                if check_valid:
                    self.play_move(user_player=user_player, move_col=int(move_output_col), move_row=int(move_output_row))
            else:
                if not 1 <= int(move_output_col) <= 3:
                    print("""
                
                INVALID COLUMN MOVE
                
                """)
                elif not 1 <= int(move_output_row) <= 3:
                    print("""
                
                INVALID ROW MOVE
                
                """)
                else:
                    print("""
                
                INVALID MOVES IN COLUMN AND ROW
                
                """)    
                self.ask_move(user_player)
        else:
            if move_output_col.isdigit():
                print("""
                
                INVALID COLUMN MOVE
                
                """)
            elif move_output_row.isdigit():
                print("""
                
                INVALID ROW MOVE
                
                """)
            else:
                print("""
                
                INVALID MOVES IN COLUMN AND ROW
                
                """)
            self.ask_move(user_player)


    def play_move(self, user_player, move_col, move_row):

        player = user_player
        self.moves[player].append((move_col, move_row))


    def record_moves(self):
        df = pd.DataFrame(self.moves)
        df.to_csv('game_history.csv')


    def check_move(self, move, user_player):
        check_result = True
        print(move, self.moves[self.player_1], self.moves[self.player_2])
        if move in self.moves[self.player_1] or move in self.moves[self.player_2]:
            print('''
            
            INVALID MOVE. 
            
            Try again.

            
            ''')
            check_result = False
            self.ask_move(user_player)
            return check_result
        else:
            return check_result




    def check_game(self, user_player):
        if (1,1) in self.moves[user_player] and (2,1) in self.moves[user_player] and (3,1) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        elif (1,1) in self.moves[user_player] and (2,2) in self.moves[user_player] and (3,3) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        elif (3,1) in self.moves[user_player] and (2,2) in self.moves[user_player] and (1,3) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        elif (1,2) in self.moves[user_player] and (2,2) in self.moves[user_player] and (3,2) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        elif (1,3) in self.moves[user_player] and (2,3) in self.moves[user_player] and (3,3) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        elif (1,1) in self.moves[user_player] and (1,2) in self.moves[user_player] and (1,3) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        elif (2,1) in self.moves[user_player] and (2,2) in self.moves[user_player] and (2,3) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        elif (3,1) in self.moves[user_player] and (3,2) in self.moves[user_player] and (3,3) in self.moves[user_player]:
            self.winner = user_player
            return user_player
        else:
            return ''

