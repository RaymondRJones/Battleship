from random import randint

p1_board = []
p2_board = []
p1_ans = []
p2_ans = []
board_size = int(input("What size should the board be? 5? 6?"))
for x in range(board_size):
    p1_board.append(["O"] * board_size)
    p2_board.append(["O"] * board_size)
    p1_ans.append(["O"] * board_size)
    p2_ans.append(["O"] * board_size)


def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(1, len(board))


def random_col(board):
    return randint(1, len(board[0]))
#Sets ships, if ship already present in space, redo's
def set_ships(board, ship_count):
    while ship_count != 0:
        ship_row = random_row(board)
        ship_col = random_col(board)
        if(board[ship_row-1][ship_col-1] == "X"):
            ship_count += 1
        board[ship_row-1][ship_col-1] = "X"
        ship_count -= 1
#Checks if user guess resulted in a hit
def check_hit(ans_board, row, col):
    if ans_board[row][col] == "X":
        ans_board[row][col] = "O"
        return True
    else:
        return False
#Checks if the User is out of turns and must switch to another player
def check_Turn(turns, ans_board, ship_count):
    if turns == 3:
        print("Turn Complete")
        return True
    else:
        if ship_count == 0:
            print("You sank all of the ships!")
            return True
        else:
            print("Try to find the next ship!")
            return False

# Prints board and answer for debugging
ship_count = int(input("How many ships do you want to use?"))
p2_ship_count = ship_count
set_ships(p1_ans, ship_count)
print_board(p1_ans)
print("Space")
flag = True
# Begins Loop to begin ask player for guess
while flag == True:
    print("Welcome Player 1:")
    for turn in range(4):
        print_board(p1_board)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
        print("Turn", turn + 1)
        # Conditionals to check whether guess was correct
        if check_hit(p1_ans, guess_row-1, guess_col-1):
            print("Congratulations! It's a hit!")
            p1_board[guess_row - 1][guess_col - 1] = "X"
            ship_count -= 1
            if check_Turn(turn, p1_ans, ship_count):
                flag = False
                break;
        #handles Incorrect Inputs and Misses
        else:
            if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
                print("Oops, that's not even in the ocean.")
            elif p1_board[guess_row - 1][guess_col - 1] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                p1_board[guess_row - 1][guess_col - 1] = "X"
            if check_Turn(turn, p1_ans, ship_count):
                break
            # Print (turn + 1) here!
            print_board(p1_board)

    if flag:
        print("Player 2's turn:")
        for turn in range(4):
            print_board(p2_board)
            guess_row = int(input("Guess Row: "))
            guess_col = int(input("Guess Col: "))
            print("Turn", turn + 1)
            # Conditionals to check whether guess was correct
            if check_hit(p2_ans, guess_row-1, guess_col-1):
                print("Congratulations! You sunk a ship!")
                p2_board[guess_row - 1][guess_col - 1] = "X"
                p2_ship_count -= 1
                if check_Turn(turn, p2_ans, p2_ship_count):
                    flag = False
                    break
            else:
                if (guess_row < 1 or guess_row > 5) or (guess_col < 1 or guess_col > 5):
                    print("Oops, that's not even in the ocean.")
                elif p2_board[guess_row - 1][guess_col - 1] == "X":
                    print("You guessed that one already.")
                else:
                    print("You missed my battleship!")
                    p2_board[guess_row - 1][guess_col - 1] = "X"
                if check_Turn(turn, p2_ans, p2_ship_count):
                    break
                # Print (turn + 1) here!
                print_board(p2_board)
