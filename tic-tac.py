import math
import time

board=[" " for _ in range(9)]
def print_board():
    print(f"{board[0]} |{board[1]} |{board[2]} ")
    print("---------")
    print(f"{board[3]} |{board[4]} |{board[5]} ")
    print("---------")
    print(f"{board[6]} |{board[7]} |{board[8]} ")

def check_winners(player):
    combos=[[0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],   
        [0,4,8], [2,4,6]  ]

    for win in combos:
        if all(board[i]==player for i in win ):
            return True
    return False

def main():
    player="o"
    print("*******************TIC-TAC-TOE*********************")
    print_board()

    while True:
        s=int(input(f"player {player} choose a spot in 1-9 : "))
        if not 1<=s<=9:
            print("invalid")
            continue
        s=s-1

        if board[s]!=" ":
            print("spot is taken")
            continue

        board[s]=player
        print_board()

        if check_winners(player):
            print(f"player {player} wins!")
            break

        if " " not in board:
            print("DRAW!")
            break

        player="o" if player=="x" else "x"





main()