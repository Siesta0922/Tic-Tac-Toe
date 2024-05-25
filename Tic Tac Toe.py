from random import randrange

# Function to display the game board
def display_board(board):
    board_template = """
+-------+-------+-------+
|       |       |       |
|   {}   |   {}   |   {}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {}   |   {}   |   {}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {}   |   {}   |   {}   |
|       |       |       |
+-------+-------+-------+
"""
    flattened_board = [board[row][col] for row in range(3) for col in range(3)]
    print(board_template.format(*flattened_board))

# Function to enter the player's move
def enter_move(board):
    while True:
        move = input("Enter your move: ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            row, col = move // 3, move % 3
            if board[row][col] not in ['O', 'X']:
                board[row][col] = 'O'
                break
            else:
                print("Field already occupied - repeat your input!")
        else:
            print("Invalid move - repeat your input!")

# Function to create a list of free fields
def get_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['O', 'X']]

# Function to check for victory
def check_victory(board, sign):
    winning_combinations = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    if [sign, sign, sign] in winning_combinations:
        return 'you' if sign == 'O' else 'me'
    return None

# Function for the computer to make a move
def draw_move(board):
    free_fields = get_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

# Initialize the game board with numbers
game_board = [[3 * row + col + 1 for col in range(3)] for row in range(3)]
game_board[1][1] = 'X'

# Main game loop
human_turn = True
while get_free_fields(game_board):
    display_board(game_board)
    if human_turn:
        enter_move(game_board)
        winner = check_victory(game_board, 'O')
    else:
        draw_move(game_board)
        winner = check_victory(game_board, 'X')
    if winner:
        break
    human_turn = not human_turn

display_board(game_board)

# Announce the result
if winner == 'you':
    print("You won!")
elif winner == 'me':
    print("I won!")
else:
    print("Tie!")
