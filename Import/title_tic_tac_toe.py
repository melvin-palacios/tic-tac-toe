
board = {1: 'T', 2: 'I', 3: 'C',
         4: 'T', 5: 'A', 6: 'C',
         7: 'T', 8: 'O', 9: 'E'}


def print_tic():
    trois = [1, 2, 3]
    a = 1
    print("         \033[0;20;40m+", end="")
    for i in trois:
        print("~~~~~+~~~~~+", end="")
    print(" ")
    print("         |", end="")
    for i in trois:
        print("           |", end="")
    print(" ")
    print("         +", end="")
    for i in trois:
        print(f"     {board[a]}     +", end="")
        a += 1
    print(" ")
    print("         |", end="")
    for i in trois:
        print("           |", end="")
    print(" ")
    print("         +", end="")
    for i in trois:
        print("~~~~~+~~~~~+", end="")

def print_tac():
    trois = [1, 2, 3]
    a = 4
    print("         \033[0;31;40m", end="")
    print(" ")
    print("         |", end="")
    for i in trois:
        print("           |", end="")
    print(" ")
    print("         +", end="")
    for i in trois:
        print(f"     {board[a]}     +", end="")
        a += 1
    print(" ")
    print("         |", end="")
    for i in trois:
        print("           |", end="")
    print(" ")
    print("         +", end="")
    for i in trois:
        print("~~~~~+~~~~~+", end="")


def print_toe():
    trois = [1, 2, 3]
    a = 7
    print("         \033[0;37;40m", end="")
    print(" ")
    print("         |", end="")
    for i in trois:
        print("           |", end="")
    print(" ")
    print("         +", end="")
    for i in trois:
        print(f"     {board[a]}     +", end="")
        a += 1
    print(" ")
    print("         |", end="")
    for i in trois:
        print("           |", end="")
    print(" ")
    print("         +", end="")
    for i in trois:
        print("~~~~~+~~~~~+", end="")
    print("")
    print("\033[0;20;40m")
def print_board_colored():
    print_tic()
    print_tac()
    print_toe()
print_board_colored()