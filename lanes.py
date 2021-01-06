def game_board(a01='  ',a02='  ',a03='  ',a11='  ',a12='  ',a13='  ',a21='  ',a22='  ',a23='  ',a31='  ',a32='  ',a33='  ',
b01='  ',b02='  ',b03='  ',b11='  ',b12='  ',b13='  ',b21='  ',b22='  ',b23='  ',b31='  ',b32='  ',b33='  '):
    '''(str,str,str,...)  
    Print a game board to display the cards, there will be 12 entrys (4 lines in 3 lanes). 
    Sometimes we can have two cards on the same entry, they will be separated by 2 spaces.
    If the entry has no cards it will be filled with 2 spaces.
    '''
    print('|        ',a01,'       |        ',a02,'       |        ',a03,'       |')
    print('|     ',a11,a12,a13,'    |     ',a21,a22,a23,'    |     ',a31,a32,a33,'    |')
    print('-'*62)
    print('|     ',b11,b12,b13,'    |     ',b11,b12,b13,'    |     ',b11,b12,b13,'    |')
    print('|        ',b01,'       |        ',b02,'       |        ',b03,'       |')


