class ChessPieces:
    def __init__(self, array):
        self.king = []
        self.pieces = []
        self.board_size = len(array)

def checkmate(board):
    try:
        array = board.split()
        if not array:
            return print("Error")

        king_count = sum(row.count("K") for row in array)
        if king_count != 1:
            return print("Error")

        for row in array:
            if len(row) != len(array):
                return print("Error")

        Chess = ChessPieces(array)
        for row in range(len(array)):
            for col in range(len(array[0])):
                if array[row][col] == "K":
                    Chess.king = [row, col]
                elif array[row][col] in {"P", "R", "B", "Q"}:
                    Chess.pieces.append([row, col])

        if check_all(array, Chess):
            print("Success")
        else:
            print("Fail")
    except Exception as e:
        print(f"Error with exception: {e}")

def check_all(array, Chess):
    for row in range(len(array)):
        for col in range(len(array[0])):
            piece = array[row][col]
            if piece == "P" and check_pawns(Chess, row, col):
                return True
            elif piece == "R" and check_rooks(Chess, row, col):
                return True
            elif piece == "B" and check_bishops(Chess, row, col):
                return True
            elif piece == "Q" and check_queens(Chess, row, col):
                return True
    return False

def check_pawns(Chess, row, col):
    if [row - 1, col - 1] == Chess.king or [row - 1, col + 1] == Chess.king:
        return True
    return False

def check_rooks(Chess, row, col):
    for direction in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if walk_to_king(direction[0], direction[1], Chess, row, col):
            return True
    return False

def check_bishops(Chess, row, col):
    for direction in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
        if walk_to_king(direction[0], direction[1], Chess, row, col):
            return True
    return False

def check_queens(Chess, row, col):
    return check_rooks(Chess, row, col) or check_bishops(Chess, row, col)

def walk_to_king(dir_row, dir_col, Chess, row, col):
    step = 1
    while step < Chess.board_size:
        move_row = row + dir_row * step
        move_col = col + dir_col * step
        if not (0 <= move_row < Chess.board_size and 0 <= move_col < Chess.board_size):
            return False
        if [move_row, move_col] == Chess.king:
            return True
        elif [move_row, move_col] in Chess.pieces:
            return False
        step += 1
    return False