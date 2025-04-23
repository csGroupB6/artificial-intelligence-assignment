
import math
import copy
import time

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of X's and O's
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    
    # X goes first, so if counts are equal, it's X's turn
    return X if count_x <= count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    
    # Check all cells and add empty ones to possible actions
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
                
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Ensure the action is valid
    if action not in actions(board):
        raise Exception("Invalid action")
    
    # Create a deep copy of the board
    new_board = copy.deepcopy(board)
    
    # Make the move
    i, j = action
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    
    # Check columns
    for j in range(3):
        if [board[i][j] for i in range(3)].count(X) == 3:
            return X
        if [board[i][j] for i in range(3)].count(O) == 3:
            return O
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game is over if there's a winner
    if winner(board) is not None:
        return True
    
    # Game is over if all cells are filled
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # X wants to maximize the utility
        best_val = -math.inf
        best_action = None
        
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_action = action
                
        return best_action
    
    else:
        # O wants to minimize the utility
        best_val = math.inf
        best_action = None
        
        for action in actions(board):
            val = max_value(result(board, action))
            if val < best_val:
                best_val = val
                best_action = action
                
        return best_action


def max_value(board):
    """
    Returns the maximum utility value for X.
    """
    if terminal(board):
        return utility(board)
    
    v = -math.inf
    
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    
    return v


def min_value(board):
    """
    Returns the minimum utility value for O.
    """
    if terminal(board):
        return utility(board)
    
    v = math.inf
    
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    
    return v


def print_board(board):
    """
    Prints the board in a readable format.
    """
    for row in board:
        print("|", end="")
        for cell in row:
            if cell == EMPTY:
                print("   |", end="")
            else:
                print(f" {cell} |", end="")
        print("\n-------------")
    #time.sleep(5)


def play_game():
    """
    Play a game of Tic Tac Toe against the AI.
    """
    board = initial_state()
    print("Welcome to Tic Tac Toe!")
    print("You are X, the computer is O.")
    print_board(board)
    
    while not terminal(board):
        # Human's turn (X)
        if player(board) == X:
            valid_move = False
            while not valid_move:
                try:
                    row = int(input("Enter row (0, 1, or 2): "))
                    col = int(input("Enter column (0, 1, or 2): "))
                    action = (row, col)
                    
                    if action in actions(board):
                        valid_move = True
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter numbers between 0 and 2.")
            
            board = result(board, action)
        
        # Computer's turn (O)
        else:
            print("Computer is thinking...")
            action = minimax(board)
            board = result(board, action)
            print(f"Computer chooses: {action}")
        
        print_board(board)
        
    # Game over
    win = winner(board)
    if win:
        print(f"Player {win} wins!")
    else:
        print("It's a draw!")


def play_tic_tac_toe_simulation():
    """
    Simulates a full game of Tic Tac Toe with both players using minimax.
    """
    board = initial_state()
    print("Initial board:")
    print_board(board)
    
    move_number = 1
    while not terminal(board):
        current_player = player(board)
        action = minimax(board)
        board = result(board, action)
        
        print(f"\nMove {move_number}: Player {current_player} places at {action}")
        print_board(board)
        move_number += 1
    
    # Game over
    win = winner(board)
    if win:
        print(f"Player {win} wins!")
    else:
        print("It's a draw!")


# Uncomment the line below to play against the computer
#play_game()

# Uncomment the line below to see a simulation of two perfect players
play_tic_tac_toe_simulation()




