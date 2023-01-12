from random import randint

# variable
case = 0

# Tableau
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def print_board():

    print("\n\n+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+")
    print(f"|  {board[1]}  |  {board[2]}  |  {board[3]}  |                   |  a  |  b  |  c  |")
    print("+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+")
    print(f"|  {board[4]}  |  {board[5]}  |  {board[6]}  |      aide   -->   |  d  |  e  |  f  |")
    print("+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+")
    print(f"|  {board[7]}  |  {board[8]}  |  {board[9]}  |                   |  g  |  h  |  i  |")
    print("+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+\n")


# ask
def ask(i):
    j = 1
    reponse_ask = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    symbole = ["X", "O"]
    current_symbol = symbole[i % len(symbole)]
    if current_symbol == "X":
        print("Joueur X")
    elif current_symbol == "O":
        print('Joueur O')
    reponse = input("quelle case voulez vous remplir ? \n")
    for a in reponse_ask:
        if a == reponse:
            if board[j] == " ":
                board[j] = current_symbol
            else:
                print("cette case est deja prise")
                ask(i)
        j+=1


# check
def checkcol():
    result = 0
    i = 0
    a = 1
    b = 4
    c = 7
    while i < 3:
        if (board[a]+board[b]+board[c] == "XXX"):
            result += 1
        elif (board[a]+board[b]+board[c] == "OOO"):
            result += 2
        else:
            result += 0
        a+=1
        b+=1
        c+=1
        i+=1
    return result


def checkli():
    result = 0
    i = 0
    a = 1
    b = 2
    c = 3
    while i < 3:
        if (board[a] + board[b] + board[c] == "XXX"):
            result += 1
        elif (board[a] + board[b] + board[c] == "OOO"):
            result += 2
        else:
            result += 0
        a += 3
        b += 3
        c += 3
        i += 1
    return result


def checkdia():
    result = 0
    i = 0
    while i < 1 :
        if board[3] + board[5] + board[7] == "XXX":
            result = 1
        elif board[3] + board[5] + board[7] == "OOO":
            result = 2
        elif board[1] + board[5] + board[9] == "XXX":
            result = 1
        elif board[1] + board[5] + board[9] == "OOO":
            result = 2
        else:
            result = 0
        i+=1
    return result

def check():
    result = 0
    result += checkli()
    result += checkdia()
    result += checkcol()
    return result


# fin
def fin(result):
    if result == 3:
        print("égalité")
    elif result == 1:
        print(f"Les croix ont gagnées !")
    elif result == 2:
        print("Les rond ont gagnées !")
    return result


# win
def win(result):
    jeu = True
    if result == 3:
        jeu = False
    elif result == 1:
        jeu = False
    elif result == 2:
        jeu = False
    return jeu


# jeu
def tic_tac_toe():
    i = randint(0, 1)
    tours = 0
    while win(check()) == True:
        print_board()
        ask(i)
        print_board()
        i += 1
        tours += 1
        if tours == 9:
            print("égalité")
            break
        fin(check())
    print("Fin du jeu")


tic_tac_toe()
