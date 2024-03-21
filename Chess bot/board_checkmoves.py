import chess

pieceDict = {
        "pawn" : "p",
        "tower" : "r",
        "knight" : "n",
        "bishop" : "b",
        "queen" : "q",
        "king" : "k"
    }

columnDict = {
        0 : "a",
        1 : "b",
        2 : "c",
        3 : "d",
        4 : "e",
        5 : "f",
        6 : "g",
        7 : "h"
    }

def piecesOnBoard(board):
    colors={
        True:0,
        False:0
    }
    for i in chess.SQUARES:
        piece = board.piece_at(i)
        if piece == None:continue
        if str(piece) == str(piece).upper():
            colors[True]+=1
        else:
            colors[False]+=1

    return colors

def countPieces(board):
    colors={
        "white":0,
        "black":0
    }

    weights={
    6:900,
    5:90,
    4:50,
    3:30,
    2:30,
    1:10
    }

    for i in chess.SQUARES:
        piece = board.piece_at(i)
        if piece == None: continue
        if str(piece) == str(piece).upper(): 
            colors["white"]+=weights.get(int(piece.piece_type))
            for j in board.attackers(chess.WHITE,i):
                piecedef = board.piece_at(j)
                colors["white"]+=int(piecedef.piece_type)
            for j in board.attackers(chess.BLACK,i):
                pieceatk = board.piece_at(j)
                colors["white"]-=int(pieceatk.piece_type)

        else: 
            colors["black"]+=weights.get(int(piece.piece_type))
            for j in board.attackers(chess.BLACK,i):
                piecedef = board.piece_at(j)
                colors["black"]+=int(piecedef.piece_type)
            for j in board.attackers(chess.WHITE,i):
                pieceatk = board.piece_at(j)
                colors["black"]-=int(pieceatk.piece_type)
    
    return colors


def generateBoard(board,turno):
    boardString=""

    for row in board:
        count = 0
        for index,column in enumerate(row):
            if column is None:
                count+=1
                if index==7:
                    boardString+=str(count)
            else:
                if count>0:
                    boardString+=str(count)
                    count=0
                boardString+=pieceDict.get(column[1]).upper() if column[0] == "white" else pieceDict.get(column[1])
                
        boardString+="/"
    boardString = boardString[:-1] + " "
    boardString += "w " if turno == "white" else "b "
    boardString += "- - 0 1"
    return chess.Board(boardString)

def getMoves(board,turno,x,y, count):

    board = generateBoard(board,turno)

    if x != None and y != None:
        pos = columnDict.get(x) + str(int(8-y))
        return getPieceMoves(board, pos)
    else:
        moves = []
        for move in board.legal_moves:
            aux = str(move)[2:]
            rowTo = 8-int(aux[1:])
            columnTo = list(columnDict.keys())[list(columnDict.values()).index(aux[:1])]
            moves.append((rowTo,columnTo))


def generateMove(move):
    try:
        aux = str(move)[:4]
        rowFrom = 8-int(aux[1])
        columnFrom = list(columnDict.keys())[list(columnDict.values()).index(aux[0])]
        rowTo = 8-int(aux[3])
        columnTo = list(columnDict.keys())[list(columnDict.values()).index(aux[2])]
        return (rowFrom,columnFrom), (rowTo,columnTo)
    except:
        print(str(move))
        return None, None



def getPieceMoves(board, fromPos):
    moves=[]
    for move in board.legal_moves:
        if fromPos in str(move):
            if len(str(move))>4:
                 aux = str(move)[:4].replace(fromPos,"")
            else:
                aux = str(move).replace(fromPos,"")
            rowTo = 8-int(aux[1:])
            columnTo = list(columnDict.keys())[list(columnDict.values()).index(aux[:1])]
            moves.append((rowTo,columnTo))
    return moves

