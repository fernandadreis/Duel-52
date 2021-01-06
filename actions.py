def draw_card(draw_pile, end_game):
    '''list, bool -> list, deck.Card, bool
    Draw one card of the draw-pile every start of turn. In this we return the new 
    draw-pile, the card that was draw for the player and tells if we are in the end-game fase(draw-pile is empty).
    '''
    n = len(draw_pile)
    draw_pile = draw_pile[0:n]
    card = draw_pile[-1]
    if n == 1:
        draw_pile = []
        end_game = True
        print('START: End Game')
    return draw_pile, card, end_game


def show_actions(e1,e2,e3,base_1,base_2,base_3,end_game):
    ''' (str, str, str, str) -> Print
    Show what actions the player can do. True for those they can do and False for those they can not do.
    '''
    play_card = False
    flip_card = False
    attack = False
    pair = False
    
    # condition for play_card
    if e1 == '' or e2 == '' or e3 == '':
        play_card = True
    
    # condition for flip_card 
    # any card on the front is face-down 
    if e1 == '??' or e2 == '??' or e3 == '??':
        flip_card = True
    # if the draw_pile is empty(end-game),they can turn the base cards if they still face-down
    if end_game == True:
        if base_1 == '??' or base_2 == '??' or base_3 == '??':
            flip_card = True

    # condition for attack
    # there is a card on the opponent field in the same lane as a face-up card on the players field 
    # 1-check if there is a face-up card 2-check if there is a card on the same lane 
    

# check for the number of True (n)

# print('You have ',n,'types of actions you can do:',)


# check the options that the player is able to do and give them to him

# play a card face-down
    # put ?? on the place that the card was placed 
    # conditon: there is a empty space ('') to put a face-down card 

# flip a card on the board
    # change ?? to the card
    # if the card has any power, activate it

# attack an opponent's card
    # see if the opponent's card has any passive power, if so, activate the power
    # check if the attacking card is a pair, if so, kill the opponent's card -> see if the card has a power when they are killed and activate it
    # if it is not a pair, check if the card has already been damaged
        # yes -> kill card (remove) -> see if the card has a power when they are killed and activate it
        # no -> deal damage to the card

# create a pair
    # put the cards together on the game board

# passive power ---- see powers
