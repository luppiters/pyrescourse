#Tic-tac-toe (or noughts and crosses) is a simple strategy game in which two players take turns placing a mark on a 3x3 board,
#attempting to make a row, column, or diagonal of three with their mark. In this homework, we will use the tools we've covered
#in the past two weeks to create a tic-tac-toe simulator and evaluate basic winning strategies.#


##Step 1##

#For our tic-tac-toe board, we will use a numpy array with dimension 3 by 3. 
#Make a function create_board() that creates such a board, with values of integers 0.
#Call create_board(), and store this as board.

import numpy

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

board = create_board()

##STEP 2##
#Players 1 and 2 will take turns changing values of this array from a 0 to a 1 or 2, indicating the number of the player 
#who places there. Create a function place(board, player, position) with player being the current player (an integer 1 or 2),
#and position a tuple of length 2 specifying a desired location to place their marker. Only allow the current player to place
#a piece on the board (change the board position to their number) if that position is empty (zero).
#Use create_board() to store a board as board, and use place to have Player 1 place a piece on spot (0, 0).

def create_board():
    board = np.zeros((3,3), dtype = int)
    return board

board = create_board()

def place(board, player, position):
    if board[position] == 0:
        board[position] = player
        return board
        
place(board, 1, (0,0))

##STEP 3##
#Create a function possibilities(board) that returns a list of all positions (tuples) on the board that are not occupied (0).
#(Hint: numpy.where is a handy function that returns a list of indexes that meet a condition.)
#board is already defined from previous exercises. Call possibilities(board) to see what it returns!

# write your code here!
import numpy 

def possibilities(board):
    return list(numpy.where(board == 0))
possibilities(board)

##code dc uses later on is: return list(zip(*np.where(board == 0)))##

##STEP 4##
#Write a function random_place(board, player) that places a marker for the current player at random among all the available
#positions (those currently set to 0).
#Find possible placements with possibilities(board).
#Select one possible placement at random using random.choice(selection).
#board is already defined from previous exercises. Call random_place(board, player) to place a random marker for Player 2,
#and store this as board to update its value.

def random_place(board, player):
    selections = possibilities(board)
    if len(selections) > 0:
        selections = random.choice(selections)
        place(board, player, selections)
    return board

random_place(board, 2)


##STEP 5##
#board is already defined from previous exercises. Use random_place(board, player) to place three pieces on board each
#for players 1 and 2.
#Print board to see your result.

board = create_board()
for i in range(3):
    for player in [1, 2]:
        random_place(board, player)

print(board)

##STEP 6##
#Now that players may place their pieces, how will they know they've won? Make a function row_win(board, player)
#that takes the player (integer), and determines if any row consists of only their marker. 
#Have it return True of this condition is met, and False otherwise.
#board is already defined from previous exercises. Call row_win to check if Player 1 has a complete row.

def row_win(board, player):
    winner = False
    if np.any(np.all(board==player, axis=1)):
        return True
    else:
        return False

row_win(board,1)

##STEP 7##
#Create a similar function col_win(board, player) that takes the player (integer), and determines if any column consists
#of only their marker. Have it return True if this condition is met, and False otherwise.
#board is already defined from previous exercises. Call col_win to check if Player 1 has a complete column.

# write your code here!
def col_win(board,player):
    winner = False
    if np.any(np.all(board==player,axis=1)):
        return True
    else:
        return False

col_win(board, 1)

#NOTE: alternative no first line, then axis=0

def col_win(board,player):
    if np.any(np.all(board==player,axis=0)):
        return True
    else:
        return False

col_win(board, 1)

##STEP 8 ##
#Finally, create a function diag_win(board, player) that tests if either diagonal of the board consists of only their marker.
#Have it return True if this condition is met, and False otherwise.
#board is already defined from previous exercises. Call diag_win to check if Player 1 has a complete diagonal.

def diag_win(board, player):
    if np.all(np.diag(board==player)):
        return True
    else:
        return False
        
diag_win(board, 1)

##STEP 9##
#Create a function evaluate(board) that uses row_win, col_win, and diag_win functions for both players.
#If one of them has won, return that player's number. If the board is full but no one has won, return -1. Otherwise, return 0.
#board is already defined from previous exercises. Call evaluate to see if either player has won the game yet.

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

# add your code here.
evaluate(board)


##STEP 10##
#create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises. 
#Create a function play_game() that creates a board, calls alternates between two players (beginning with Player 1), 
#and evaluates the board for a winner after every placement. 
#Play the game until one player wins (returning 1 or 2 to reflect the winning player), or the game is a draw (returning -1).
#Call play_game once.

def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1,2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
            
    return winner
    
play_game()

##STEP 11##

#Use the play_game() function to play 1,000 random games, where Player 1 always goes first.
#When doing this, import and use the time library to call the time function both before and after playing all 1,000 games
#in order to evaluate how long this takes per game. Print your answer.
#The library matplotlib.pyplot has already been stored as plt. Use plt.hist and plt.show to plot a histogram of the results.
#Does Player 1 win more than Player 2? Does either player win more than each player draws?

import time
import matplotlib.pyplot as plt

start = time.time()

games = [play_game() for i in range(1000)]

end = time.time()
print(end-start)

plt.hist(games)

plt.show()

#Great work! We see that Player 1 wins more than Player 2, and the game sometimes ends in draws.#
#The total amount of time taken is about a few seconds, but will vary from machine to machine.#

##STEP 12##
#This result is expected --- when guessing at random, it's better to go first. Let's see if Player 1 can improve their strategy.
#create_board(), random_place(board, player), and evaluate(board) have been created from previous exercises.
#Create a function play_strategic_game(), where Player 1 always starts with the middle square, and otherwise both players
#place their markers randomly.
#Call play_strategic_game once.

def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            board= random_place(board,player)
        
            # use `evaluate(board)`, and store as `winner`.
            winner = evaluate(board)
            
            if winner != 0:
                break
    return winner

play_strategic_game()  

##STEP 13##
#The results from Exercise 12 have been stored. Use the play_strategic_game() function to play 1,000 random games.
#Use the time libary to evaluate how long all these games takes.
#The library matplotlib.pyplot has already been stored as plt. Use plt.hist and plt.show to plot your results. 
#Did Player 1's performance improve? Does either player win more than each player draws?

# write your code here!
import time
import matplotlib.pyplot as plt

s = time.time()

game = [play_strategic_game() for i in range(1000)]

f = time.time()

print(f-s)

plt.hist(game)
plt.show()

#Great work! Yes, starting in the middle square is a large advantage when play is otherwise random. 
#Also, each game takes less time to play, because each victory is decided earlier. 
#Player 1 wins much more than Player 2, and draws are less common.#
