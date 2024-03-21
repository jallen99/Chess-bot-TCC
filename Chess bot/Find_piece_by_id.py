
def find_piece_position(board,id):
    for y in range(8):
        for x in range(8):
            if board[y][x]!= None and board[y][x][3] == id:
                return (y,x)
    return False