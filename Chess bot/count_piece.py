import pygame
import time

weights={
    "king":900,
    "queen":90,
    "tower":50,
    "bishop":30,
    "knight":30,
    "pawn":10
    }


def count_piece(board):
    scores={
        'white':0,
        'black':0
    }

    white_pieces={
        "king":0,
        "queen":0,
        "tower":0,
        "bishop":0,
        "knight":0,
        "pawn":0
    }

    black_pieces={
        "king":0,
        "queen":0,
        "tower":0,
        "bishop":0,
        "knight":0,
        "pawn":0

    }


    for i in range(8):
        for j in range(8):
            if not(board[i][j] is None):
                scores[board[i][j][0]]+= weights.get(board[i][j][1])
                if board[i][j][0] == 'white':
                    white_pieces[board[i][j][1]]+=1
                else:
                    black_pieces[board[i][j][1]]+=1

    return scores

