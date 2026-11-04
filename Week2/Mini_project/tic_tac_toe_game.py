board = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
def display_board():
    for index, row in enumerate(board):
        print (" | ".join(row))

        if index <2:
            print ("--+---+--")
display_board()

def player_input(player):
    while True:
        try:
            row=int(input("Enter row (1-3): "))
            col=int(input("Enter column (1-3): "))
        except ValueError:
            print("Please enter numbers!")    
        if 1<=row<=3 and 1<=col<=3:
            if board[row-1][col-1]==" ":
                board[row-1][col-1]=player
                break
            else:
                print("Cell is ocupied")
        else:
            print("Invalid input")
player_input("X")
display_board()
def check_win(board, player):
    for row in board:
        if row[0]==player and row[1]==player and row[2]==player:
            return True
    return False
