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
    reponse = input("quelle case voulez vous remplir ? ")

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

# IA

def iacol():
    ia_symbole = "O"
    result = 0
    i = 0
    a = 1
    b = 4
    c = 7
    while i < 3:
        if board[a] + board[b] + board[c] == "XX ":
            if board[c] == " ":
                board[c] = ia_symbole
        elif board[a] + board[b] + board[c] == " XX":
            if board[a] == " ":
                board[a] = ia_symbole
        elif board[a] + board[b] + board[c] == "X X":
            if board[b] == " ":
                board[b] = ia_symbole
        else:
            result += 0
        a += 1
        b += 1
        c += 1
        i += 1


def iali():
    ia_symbole = "O"
    result = 0
    i = 0
    a = 1
    b = 2
    c = 3
    while i < 3:
        if board[a] + board[b] + board[c] == "XX ":
            if board[c] == " ":
                board[c] = ia_symbole
        elif board[a] + board[b] + board[c] == " XX":
            if board[a] == " ":
                board[a] = ia_symbole
        elif board[a] + board[b] + board[c] == "X X":
            if board[b] == " ":
                board[b] = ia_symbole


        else:
            result += 0
        a += 3
        b += 3
        c += 3
        i += 1


def iadia():
    i = 0
    ia_symbole = "O"
    while i < 1:
        if board[3] + board[5] + board[7] == "X X":
            if board[5] == " ":
                board[5] = ia_symbole
        elif board[3] + board[5] + board[7] == "XX ":
            if board[7] == " ":
                board[7] = ia_symbole
        elif board[3] + board[5] + board[7] == " XX":
            if board[3] == " ":
                board[3] = ia_symbole
        elif board[1] + board[5] + board[9] == "X X":
            if board[5] == " ":
                board[5] = ia_symbole
        elif board[1] + board[5] + board[9] == " XX":
            if board[1] == " ":
                board[1] = ia_symbole
        elif board[1] + board[5] + board[9] == "XX ":
            if board[9] == " ":
                board[9] = ia_symbole
        i += 1


def randomcase():
    i = randint(1, 9)
    if board[5] == " ":
        board[5] = "O"
    elif board[i] == " ":
        board[i] = "O"
    else:
        randomcase()


def ia_impo():
    if check() == 0:
        iali()
        iacol()
        iadia()
    else:
        randomcase()


# jeu
def tic_tac_toe():
    i = randint(0, 1)
    tours = 0
    nb_joueur = input("Veuillez entrer le nombre de joueur (1 ou 2) ")
    if nb_joueur == "1":
        i = 0
        dif = input("Choissisez la dificulté :\n a) moyenne\n b) impossible ")
        if dif == "a":
            while win(check()) == True:
                fin(check())
                print_board()
                ask(i)
                fin(check())
                tours += 1
                randomcase()
                tours += 1
                if tours == 9:
                    print("égalité")
                    break
            print("Fin du jeu")
        elif dif == "b":
            while win(check()) == True:
                fin(check())
                print_board()
                ask(i)
                fin(check())
                tours += 1
                ia_impo()
                tours += 1
                if tours == 9:
                    print("égalité")
                    break
            print("Fin du jeu")
        else:
            print("Erreur")
            tic_tac_toe()
    elif nb_joueur == "2":
        while win(check()) == True:
            print_board()
            ask(i)
            fin(check())
            i+=1
            tours +=1
            if tours == 9:
                print("égalité")
                break
        print("Fin du jeu")
    else:
        print("Erreur")
        tic_tac_toe()


tic_tac_toe()
