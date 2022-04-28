
#Ana Cecilia Llarena
#Hoja de Trabajo Tic Tac Toe

'''
Tic-tac-toe game utils.
'''


def create_empty_board():

    board = []
    for i in range(3):
        board.append([None] * 3)

    return board


def print_board(board):

    print('\n'.join([str(row) for row in board]))

#Nuevo movimiento del jugador
def update_board(board, position, player):
    board[position[0]][position[1]] = player
    return board
    
def check_for_winner(board, player):


    if (board[0][0] == player and board[0][1] == player and board[0][2] == player):
        return True

    elif (board[1][0] == player and board[1][1] == player and board[1][2]== player):
        return True
    
    elif (board[2][0] == player and board[2][1] == player and board[2][2]== player):
        return True

    elif (board[0][0] == player and board [1][0] == player and board [2][0] == player):
        return True

    elif (board[0][1] == player and board [1][1]== player and board [2][1] == player):
        return True

    elif (board[0][2] == player and board [1][2] == player and board [2][2] == player):
        return True

    elif (board[0][0] == player and board[1][1] == player and board[2][2]== player):
        return True

    elif (board[0][2] == player and board[1][1] == player and board[2][0]== player):
        return True

    else:
        return False


'''
Testing: 
'''
board = create_empty_board()
print_board(board)
update_board(board, [0,2], "0")
update_board(board, [1,1], "X")
update_board(board, [2,1], "0")
update_board(board, [0,1], "X")
update_board(board, [1,0], "0")
update_board(board, [2,0], "X")

#Imprimiendo resultado del board vacío
print_board(board)

#Imprimiento resultado del board jugando
print(check_for_winner(board, "X"))
