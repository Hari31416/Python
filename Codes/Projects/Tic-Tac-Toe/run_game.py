from funcs import *

print('Welcome to Tic Tac Toe!')
while start_play():
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(board)
    turn = choose_first()
    marker1 , marker2 = player_input()
    flage = True
    
    while flage:

        if turn == 1:
            # First Player
            print("First Player's turn!")
            position = player_choice(board)
            place_marker(board, marker1, position)
            display_board(board)
            if win_check(board, marker1):
                print("First player Won!")
                break
            else:
                turn = 2
            if full_board_check(board):
                print("It's a draw!")
                break
            
        elif turn == 2:
            # First Player
            print("Second Player's turn!")
            position = player_choice(board)
            place_marker(board, marker2, position)
            display_board(board)
            if win_check(board, marker2):
                print("Second player Won!")
                break
            else:
                turn = 1
            if full_board_check(board):
                print("It's a draw!")
                break
            