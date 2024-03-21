from typing import Match
import move_piece as mp
import count_piece as cp
import check_checkmate_draw as vc
import math
import copy
import random
import time
import pawn_promotion as pp
import board_checkmoves
import chess

def evaluate(board,maximizing_color):
    try:
        board_aux = board_checkmoves.generateBoard(board,maximizing_color)
    except:
        board_aux = board
    score = board_checkmoves.countPieces(board_aux)
    if maximizing_color == 'white':
        return score.get('white') - score.get('black')
    else:
        return score.get('black') - score.get('white')

def verify_all_possible_moves(board,color):

    all_movements = []
    for y in range(8):
        for x in range(8): 
            piece = board[y][x]
            selected_piece = piece, x, y

            if selected_piece[0] != None and piece[0] == color:
                possible_moves = board_checkmoves.getMoves(board, color, x, y, 0)

                movements = {
                    "possible_moves": possible_moves,
                    "color":piece[0],
                    "piece_id":piece[3],
                    "piece_type":piece[1],
                    "piece_image":piece[2],
                    "piece_position":(y,x)
                }
                if movements["possible_moves"]:
                    all_movements.append(movements)
    print(all_movements)
    return all_movements

    
def minimax (board, depth,alpha,beta, maximizing_player):

    if depth == 0 or board.is_checkmate() or len(list(board.legal_moves))==0:  
        return None, evaluate(board,maximizing_player)

    moves = []
    piecesCount = board_checkmoves.piecesOnBoard(board)
    if maximizing_player:
        maxEval = -math.inf
        moves = board.legal_moves
        best_move = random.choice(list(moves))
        try:
            for move in moves:

                    try:
                        board.push(chess.Move.from_uci(str(move)))
                    except:
                        continue
                    if board.is_check() == False:
                        eval = minimax(board, depth - 1, alpha, beta, False)[1]

                        if eval > maxEval and board.is_check() == False:
                            maxEval = eval
                            best_move = move
                        
                        elif eval == maxEval and board.is_check() == False and board_checkmoves.piecesOnBoard(board)[(maximizing_player)]<piecesCount[(maximizing_player)]:
                            maxEval = eval
                            best_move = move


                        alpha = max(alpha,eval)
                        if beta <= alpha:
                            board.pop()
                            break       
                    board.pop()       
            return best_move,maxEval
        except IndexError as e:
            if board.is_checkmate():
                return None, evaluate(board,maximizing_player)
            else:
                print(str(e))
                print("Movimentos:", moves)
                print("Checkmate:", board.is_checkmate())
                print("Board:\n")
                print(board)
                raise Exception("Error")

    else:
        minEval = math.inf
        moves = board.legal_moves
        
        best_move = random.choice(list(moves))
        try:
            for move in moves:
                    try:
                        board.push(chess.Move.from_uci(str(move)))
                    except:
                        continue
                    if board.is_check() == False:
                        eval = minimax(board, depth - 1, alpha, beta, True)[1]
                        if eval < minEval and board.is_check() == False:
                            minEval = eval
                            best_move = move
                        
                        elif eval == minEval and board_checkmoves.piecesOnBoard(board)[(maximizing_player)]<piecesCount[(maximizing_player)]:
                            minEval = eval
                            best_move = move

                        beta = min(beta,eval)
                        if beta <= alpha:
                            board.pop()
                            break    
                    board.pop()    
            return best_move,minEval
        except IndexError as e:
            if board.is_checkmate():
                return None, evaluate(board,maximizing_player)
            else:
                print(str(e))
                print("Movimentos:", moves)
                print("Checkmate:", board.is_checkmate())
                print("Board:\n")
                print(board)
                raise Exception("Error")

def make_move(board,turno,new_position,old_position,piece):
    is_check = False
    board[old_position[0]][old_position[1]] = None
    board[new_position[0]][new_position[1]] = piece
    promoted = pp.pawn_promotion_bot(turno,piece,board,new_position[0],new_position[1])

    if vc.is_check(turno,board):
        is_check = True

    return copy.deepcopy(board),is_check, promoted

def unmake_move(board,new_position,old_position,piece, promoted):
    if promoted:
        piece[1]=='pawn'
        piece[2]== r"Images\Pawn_"+ "W.png" if piece[0]=='white' else "B.png"
    board[old_position[0]][old_position[1]] = piece
    board[new_position[0]][new_position[1]] = None

    return copy.deepcopy(board)

