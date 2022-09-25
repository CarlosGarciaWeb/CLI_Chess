from time import gmtime
from board import Board
from gameplay import GamePlay
game_board = Board()


if __name__ == "__main__":
    board_game = game_board.create_board()
    
    play_game = GamePlay('Carlos', 'Karen')
    print(play_game.game_instructions)
    print(board_game, game_board.positions)
    print(play_game.player_1, play_game.player_2)
    play_game.ask_move(play_game.player_1, 0, 7)
    print(play_game.moves)  

