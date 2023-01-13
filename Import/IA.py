from random import randint
# IA

def iacol(board):
    ia_symbole = "O"
    result = 0
    i = 0
    a = 1
    b = 4
    c = 7
    while i < 3:
        if board[a] + board[b] + board[c] == "XX ":
            board[c] = ia_symbole
            result +=1
        elif board[a] + board[b] + board[c] == " XX":
            board[a] = ia_symbole
            result += 1
        elif board[a] + board[b] + board[c] == "X X":
            board[b] = ia_symbole
            result += 1
        a += 1
        b += 1
        c += 1
        i += 1
    return result


def iali(board):
    ia_symbole = "O"
    result = 0
    i = 0
    a = 1
    b = 2
    c = 3
    while i < 3:
        if board[a] + board[b] + board[c] == "XX ":
            board[c] = ia_symbole
            result += 1
        elif board[a] + board[b] + board[c] == " XX":
            board[a] = ia_symbole
            result += 1
        elif board[a] + board[b] + board[c] == "X X":
            board[b] = ia_symbole
            result += 1
        a += 3
        b += 3
        c += 3
        i += 1
    return result


def iadia(board):
    result = 0
    i = 0
    ia_symbole = "O"
    while i < 1:
        if board[3] + board[5] + board[7] == "X X":
            board[5] = ia_symbole
            result += 1
        elif board[3] + board[5] + board[7] == "XX ":
            board[7] = ia_symbole
            result += 1
        elif board[3] + board[5] + board[7] == " XX":
            board[3] = ia_symbole
            result += 1
        elif board[1] + board[5] + board[9] == "X X":
            board[5] = ia_symbole
            result += 1
        elif board[1] + board[5] + board[9] == " XX":
            board[1] = ia_symbole
            result += 1
        elif board[1] + board[5] + board[9] == "XX ":
            board[9] = ia_symbole
            result += 1
        i += 1
    return result


def randomcase(board):
    i = randint(1, 9)
    if board[5] == " ":
        board[5] = "O"
    elif board[i] == " ":
        board[i] = "O"
    else:
        randomcase(board)

def ia_impo(board):
    total = iali(board) + iacol(board) + iadia(board)
    if total == 0:
        randomcase(board)
