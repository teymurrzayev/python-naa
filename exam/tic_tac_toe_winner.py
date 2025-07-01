def tic_tac_toe_winner(moves: list[list[int]]) -> str:
    board = [[None for _ in range(3)] for _ in range(3)]
    
    for i, move in enumerate(moves):
        row, col = move
        if i % 2 == 0:
            board[row][col] = 'X'  
        else:
            board[row][col] = 'O'  
        winner = check_winner(board)
        if winner:
            return 'A' if winner == 'X' else 'B'
    if len(moves) == 9:
        return "Draw"
    else:
        return "Pending"

def check_winner(board):
    for row in board:
        if row[0] is not None and row[0] == row[1] == row[2]:
            return row[0]
    for col in range(3):
        if board[0][col] is not None and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    if board[0][0] is not None and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not None and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None