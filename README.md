# CLI_TicTacToe


Created a tic tac toe gameplay brain and boad file that are later called through a main file. This is in order to practice OOP.


board.py has a class of Board() that creates the board on the CLI, providing instructions, and updates of how the board looks when a player chooses a position. It is based on the positions of the string, the avaiable positions are dinamically found through the first char "|" of each row, by creating a count I ensure that the first "|" is not the second one in the row when using modulo on the count number, the count is increased by 1 when a "|" is found. 

         1 2 3

      1  _|_|_
      2  _|_|_
      3   | |
      
the above is the board using triple quote pairs. Available positions are the inmediate previous position, the inmediate following position and the third position after that initial position of "|" in that row.

Example, let's take a look at row 1 and let's give hipothetical positions, the position will be right below the char:
1  _|_|_     <--- board

0123456789   <--- positions

Depending on the size of the board (i.e if there are more espaces before the       
      
