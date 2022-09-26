from time import gmtime
from board import Board
from gameplay import GamePlay
game_board = Board()


if __name__ == "__main__":
    # Create the board object
    board_game = game_board.create_board()

    # Ask for player names
    player_1 = input("Provide name for player 1: \n",)
    player_2 = input("Provide name for player 2: \n")
    # Create Gameplay object and introduce player names
    play_game = GamePlay(player_1, player_2)
    # Replace names with player objects from gameplay
    player_1 = play_game.player_1
    player_2 = play_game.player_2
    print(play_game.game_instructions)
    print(board_game, game_board.positions)
    check = True
    for _ in range(9):
        if check:
            play_game.ask_move(player_1)
            check = False
        else:
            play_game.ask_move(player_2)
            check = True
        print(play_game.moves)  

