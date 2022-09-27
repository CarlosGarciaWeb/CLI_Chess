from time import gmtime
from board import Board
from gameplay import GamePlay
game_board = Board()
print("Hello!")

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
    turn_p1 = 1
    turn_p2 = 1
    for _ in range(9):
        if check:
                  
            play_game.ask_move(player_1)
            piece = 'X'
            check = False
            played_move = play_game.moves[player_1][turn_p1-1]
            print(played_move)            
            game_board.update_board(move=played_move, piece=piece)
            play_game.check_game(player_1)
            if play_game.winner == player_1:
                print(f"{player_1} wins!")
                break
            turn_p1 += 1

        else:
            play_game.ask_move(player_2)
            piece = 'O'
            check = True
            played_move = play_game.moves[player_2][turn_p2-1]
            game_board.update_board(move=played_move, piece=piece)
            play_game.check_game(player_2)
            if play_game.winner == player_2:
                print(f'{player_2} wins!')
                break
            turn_p2 += 1
        print(play_game.moves)
    if play_game.winner == "":
        print("It's a draw!")


        
    print(play_game.moves)  

