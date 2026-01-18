
# Made by Alex von Allemann

import random

def display(TheBoard,theBoardLayout):
    
    print('   |   |')
    print(' ' + TheBoard[7] + ' | ' + TheBoard[8] + ' | ' + TheBoard[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + TheBoard[4] + ' | ' + TheBoard[5] + ' | ' + TheBoard[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + TheBoard[1] + ' | ' + TheBoard[2] + ' | ' + TheBoard[3])
    print('   |   |')
    print('')
    print('-------------')
    print('-------------')
    print('-------------')
    print('-------------')
    print('')
    print('   |   |')
    print(' ' + theBoardLayout[7] + ' | ' + theBoardLayout[8] + ' | ' + theBoardLayout[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + theBoardLayout[4] + ' | ' + theBoardLayout[5] + ' | ' + theBoardLayout[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + theBoardLayout[1] + ' | ' + theBoardLayout[2] + ' | ' + theBoardLayout[3])
    print('   |   |')

def player_input():
    
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: Do you want to be X or O? ')
        marker = marker.upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position, theboardLayout):
    board[position] = marker
    theboardLayout[position] = '*'

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


def space_check(board, position):
    
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def player_choice(board,currentplayer):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        
        position = int(input(f'{currentplayer} Choose your next position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


def main():
    print('Welcome to Tic Tac Toe game!')

    while True:
        theBoard = [' '] * 10
        theBoardLayout = ['0','1','2','3','4','5','6','7','8','9']
        player1_marker, player2_marker = player_input()
        turn = choose_first()
        print(turn + ' will go first.')
    
        play_game = input('Are you ready to play? Enter Yes or No. ')
    
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Player 1':
                display(theBoard,theBoardLayout)
                position = player_choice(theBoard,'Player 1')
                place_marker(theBoard, player1_marker, position,theBoardLayout)

                if win_check(theBoard, player1_marker):
                    display(theBoard,theBoardLayout)
                    print('Congratulations! You have won the game!')
                    game_on = False
                else:
                    if full_board_check(theBoard):
                        display(theBoard,theBoardLayout)
                        print('The game is a draw!')
                        break
                    else:
                        turn = 'Player 2'

            else:
                display(theBoard,theBoardLayout)
                position = player_choice(theBoard,'Player 2')
                place_marker(theBoard, player2_marker, position,theBoardLayout)

                if win_check(theBoard, player2_marker):
                    display(theBoard,theBoardLayout)
                    print('Player 2 has won!')
                    game_on = False
                else:
                        if full_board_check(theBoard):
                            display(theBoard,theBoardLayout)
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 1'

        if not replay():
            break

main()
