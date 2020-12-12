# using 4 or 2 spaces to right the card(s)

def game_board(a11,a12,a13,a21,a22,a23,a31,a32,a33,a41,a42,a43,a44):
    '''(str,str,str,...) -> str 
    Print a game board to display the cards, there will be 12 entrys (4 lines in 3 lanes). 
    Sometimes we can have two cards on the same entry, they will be separated by 2 spaces.
    The entrys of the game board will be treated as a matrix.
    '''
    print('|     ??     |     ??     |     ??     |')
    print('|   A♥  2♥   |     T♥     |     ??     |')
    print('-'*40)
    print('-'*40)
    print('|     ??     |     ??     |     ??     |')
    print('|     ??     |     ??     |     ??     |')
