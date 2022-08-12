from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])


def player_input():
    initial_input = ''
    while initial_input not in ['X', 'O']:
        marker = input('Please choose between X or O: ')
        if marker.lower() not in ['x', 'o']:
            print('Please give a correct input.')
        else:
            if marker.lower() == 'x':
                marker = ('X', 'O')
                break
            else:
                marker = ('O', 'X')
                break     
    return marker


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

   

def choose_first():
    player_num = random.randint(1, 2)
    print(f"Player {player_num} gets first move!")
    return player_num



def space_check(board, position):
    return board[position] == ' '

    

def full_board_check(board):
    for num in range(1, 10):
        if board[num] == ' ':
            check = False
        else:
            check =True
    return check


def player_choice(board):
    flage = True
    while flage:
        position = input('Please provide your next position (1,9): ')
        if position.isdecimal() == False or int(position) not in range(1, 10):
            print("Please provide the correct position.")
        elif space_check(board, int(position)):
            position = int(position)
            break
        else:
            print('The position you are choosing is already filled!')
    return position


def replay():
    flage = True
    while flage:
        choose = input("Do you wnat to play again? ( 'Y' or 'N') ")
        if choose.lower() != 'y' and choose.lower() != 'n':
            print('Please enter Y or N')
        else:
            break
    return choose.lower() == 'y'



def start_play():
    while True:
        choose = input("Do you want to play the game? Type 'Y' or 'N': ")
        if choose.lower() not in ['y', 'n']:
            print("Type 'y or 'n.")
        else:
            break
    return choose.lower() == 'y'