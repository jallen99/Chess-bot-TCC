import chess

board = chess.Board()
print(board.legal_moves)
for j in board.legal_moves:
    print(j)