from random import randint

p1_board = []
p2_board = []

for x in range(5):
    p1_board.append(["O"] * 5)
    p2_board.append(["O"] * 5)


def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board[0]))

def set_ships(board):
    ship_row = random_row(p1_board)
    ship_col = random_col(p1_board)

def check_Turn(turns, ship_row,ship_col, guess_row, guess_col):
  if turns == 3:
    print('Game Over')
    return True
  elif ship_row == guess_row and ship_col == guess_col:
    print("You won!")
    return True
#Prints board and answer for debugging
p1_ship_row = random_row(p1_board)
p1_ship_col = random_col(p1_board)
print_board(p1_board)
print (p1_ship_row)
print (p1_ship_col)
flag = True
#Begins Loop to begin ask player for guess
while flag == True:
    print ("Welcome Player 1:")

    for turn in range(4):
      guess_row = int(input("Guess Row: "))
      guess_col = int(input("Guess Col: "))
      print ("Turn", turn +1)
      # Conditionals to check whether guess was correct
      if guess_row == p1_ship_row and guess_col == p1_ship_col:
        print ("Congratulations! You sunk my battleship!")
        if check_Turn(turn, p1_ship_row, p1_ship_col, guess_row, guess_col):
          flag = False
          break;
      else:
        if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
          print ("Oops, that's not even in the ocean.")
        elif p1_board[guess_row - 1][guess_col - 1] == "X":
          print ("You guessed that one already.")
        else:
          print ("You missed my battleship!")
          p1_board[guess_row - 1][guess_col - 1] = "X"
        if check_Turn(turn, p1_ship_row, p1_ship_col, guess_row, guess_col):
          break
        # Print (turn + 1) here!
        print_board(p1_board)

    if flag:
      print ("Player 2's turn:")
      p2_ship_row = random_row(p2_board)
      p2_ship_col = random_col(p2_board)
      print_board(p2_board)
      print(p2_ship_row)
      print(p2_ship_col)
      for turn in range(4):
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        print ("Turn", turn +1)
        # Conditionals to check whether guess was correct
        if guess_row == p2_ship_row and guess_col == p2_ship_col:
          print ("Congratulations! You sunk my battleship!")
          if check_Turn(turn, p2_ship_row, p2_ship_col, guess_row, guess_col):
            flag = False
            break;
        else:
          if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
            print ("Oops, that's not even in the ocean.")
          elif p2_board[guess_row - 1][guess_col - 1] == "X":
            print ("You guessed that one already.")
          else:
            print ("You missed my battleship!")
            p2_board[guess_row - 1][guess_col - 1] = "X"
          if check_Turn(turn, p2_ship_row, p2_ship_col, guess_row, guess_col):
            break
          # Print (turn + 1) here!
          print_board(p2_board)