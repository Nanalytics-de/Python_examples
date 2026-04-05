import random
# board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
# run = 0
# choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]


# Say "Hello, lets play Tic-Tac-Toe"
def say_hello():
    print("Hello, let's play Tic-Ta-Toe!""\n"
          "The board looks like this""\n"
          "0 | 1 | 2""\n"
          "3 | 4 | 5""\n"
          "6 | 7 | 8""\n"
          "So lets start")
# ---------------------------------------------

# Create function for board (via a list and | )
def create_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("***********")
# ---------------------------------------------


#1.) OUTPUT: Ask Player1 = (X) to choose a number and show (board without numbers)

def player_choose(board, run, choices):
    random_choose = random.choice(choices)
 
    if run % 2 == 0:
        choose = input(f"Please choose a number from {choices}: ")
        board[int(choose)] = "X" 
        choices = choices.remove(choose)
    else:
        board[int(random_choose)] = "O"
        choices = choices.remove(random_choose)    
        
# ---------------------------------------------    

# Create function with win and draw. 
# If one player has 3 in one row, column or diagonal -> player wins. Else draw
  
def check_win(board):
    if board[0] == board[1] == board[2] and board[0] != "-":
        print(f"Player {board[0]} wins!")
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        print(f"Player {board[3]} wins!")
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        print(f"Player {board[6]} wins!")
        return True
    elif board[0] == board[3] == board[6] and board[0] != "-":
        print(f"Player {board[0]} wins!")
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        print(f"Player {board[1]} wins!")
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        print(f"Player {board[2]} wins!")
        return True
    elif board[0] == board[4] == board[8] and board[0] != "-":
        print(f"Player {board[0]} wins!")
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        print(f"Player {board[2]} wins!")
        return True
    else:
        return False
# ---------------------------------------------

# Ask player if thy want to play again
def again():
    answer = input("Do you want to play again? (y/n): " )
    if answer == "y":
        tic_tac_toe()
    elif answer == "n":
        print("Have a nice day!")
        return False
    else:
        print("Answer is not valid!")
# ---------------------------------------------

def tic_tac_toe():
    board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    run = 0
    choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    say_hello()
    while run < 9:
        player_choose(board, run, choices)
        create_board(board)
        if check_win(board):
            if again() == False:
                break
        else:
            run += 1
            if run == 9:
                print("It's a draw")
                if again() == False:
                    break
# ---------------------------------------------

# Tic-tac-toe game
tic_tac_toe()