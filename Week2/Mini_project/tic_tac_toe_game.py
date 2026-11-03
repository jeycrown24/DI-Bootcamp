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
