from random import randint

#tableau
tableau = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

#variable
jeu = True
result = 0
tours = 0
case = 0
i = randint(0, 1)

#board
def board():

    print("\n\n+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+")
    print(f"|  {tableau[0][0]}  |  {tableau[0][1]}  |  {tableau[0][2]}  |                   |  a  |  b  |  c  |")
    print("+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+")
    print(f"|  {tableau[1][0]}  |  {tableau[1][1]}  |  {tableau[1][2]}  |      aide   -->   |  d  |  e  |  f  |")
    print("+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+")
    print(f"|  {tableau[2][0]}  |  {tableau[2][1]}  |  {tableau[2][2]}  |                   |  g  |  h  |  i  |")
    print("+~~~~~+~~~~~+~~~~~+                   +~~~~~+~~~~~+~~~~~+\n")


#check
def check(tableau):
    result = 0
    croix = "X"
    rond = "O"
    # lignes
    if tableau[0][0] == croix and tableau[0][1] == croix and tableau[0][2] == croix:
        result = 1
    elif tableau[0][0] == rond and tableau[0][1] == rond and tableau[0][2] == rond:
        result = 2
    elif tableau[1][0] == croix and tableau[1][1] == croix and tableau[1][2] == croix:
        result = 1
    elif tableau[1][0] == rond and tableau[1][1] == rond and tableau[1][2] == rond:
        result = 2
    elif tableau[2][0] == croix and tableau[2][1] == croix and tableau[2][2] == croix:
        result = 1
    elif tableau[2][0] == rond and tableau[2][1] == rond and tableau[2][2] == rond:
        result = 2
    # colones
    elif tableau[0][0] == croix and tableau[1][0] == croix and tableau[2][0] == croix:
        result = 1
    elif tableau[0][0] == rond and tableau[1][0] == rond and tableau[2][0] == rond:
        result = 2
    elif tableau[0][1] == croix and tableau[1][1] == croix and tableau[2][1] == croix:
        result = 1
    elif tableau[0][1] == rond and tableau[1][1] == rond and tableau[2][1] == rond:
        result = 2
    elif tableau[0][2] == croix and tableau[1][2] == croix and tableau[2][2] == croix:
        result = 1
    elif tableau[0][2] == rond and tableau[1][2] == rond and tableau[2][2] == rond:
        result = 2
    # diagonales
    elif tableau[0][0] == croix and tableau[1][1] == croix and tableau[2][2] == croix:
        result = 1
    elif tableau[0][0] == rond and tableau[1][1] == rond and tableau[2][2] == rond:
        result = 2
    elif tableau[0][2] == croix and tableau[1][1] == croix and tableau[2][0] == croix:
        result = 1
    elif tableau[0][2] == rond and tableau[1][1] == rond and tableau[2][0] == rond:
        result = 2
    #egalité
    elif case == 9:
        result = 3
    # partie pas finie
    else:
        result = 0
    return result



def ask():
    symbole = ["X", "O"]
    current_symbol = symbole[i % len(symbole)]
    if current_symbol == "X":
        print("Joueur 1")
    elif current_symbol == "O":
        print('Joueur 2')
    reponse = input("quelle case voulez vous remplir ? ")
    if reponse == "a" and tableau[0][0] == " ":
        tableau[0][0] = current_symbol
    elif reponse == "b" and tableau[0][1] == " ":
        tableau[0][1] = current_symbol
    elif reponse == "c" and tableau[0][2] == " ":
        tableau[0][2] = current_symbol
    elif reponse == "d" and tableau[1][0] == " ":
        tableau[1][0] = current_symbol
    elif reponse == "e" and tableau[1][1] == " ":
        tableau[1][1] = current_symbol
    elif reponse == "f" and tableau[1][2] == " ":
        tableau[1][2] = current_symbol
    elif reponse == "g" and tableau[2][0] == " ":
        tableau[2][0] = current_symbol
    elif reponse == "h" and tableau[2][1] == " ":
        tableau[2][1] = current_symbol
    elif reponse == "i" and tableau[2][2] == " ":
        tableau[2][2] = current_symbol
    else:
        print("cette case est deja prise")


#fin
def fin(result):
    jeu = False
    if result == 3:
        print("égalité")
    elif result == 1:
        print(f"Les croix ont gagnées !")
        jeu = True
    elif result == 2:
        print("Les rond ont gagnées !")
        jeu = True
    return jeu
#jeu
while check(tableau) == 0:
    board()
    ask()
    board()
    i += 1
    fin(check(tableau))
    tours += 1
    if tours == 9:
        print("égalité")
        break

print("Fin du jeu")