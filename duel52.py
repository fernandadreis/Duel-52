from time import sleep
from lanes import game_board
from deck import make_deck, pick_a_card, show_cards
from actions import draw_card
deck = make_deck() # the deck of this game

# preparing to the start of the game
# flag to alert the end-game
end_game = False
# dealing cards
face_down = deck[0:6] # 1 face_down card in each lane for each player

# each player starts with 5 cards on hand
hand_player1 = deck[6:11] 
hand_player2 = deck[11:16]

draw_pile = deck[16:42] # 10 cards are removed from the deck, so the draw_pile has 26 cards

# "put the face_down cards on the board" / give a variable to the cards on the game_board 
a01 = deck[0]
a02 = deck[1]
a03 = deck[2]
b01 = deck[3]
b02 = deck[4]
b03 = deck[5]

# leave the other spaces of the board empty 
a11 = '  '
a12 = '  '
a13 = '  '
a21 = '  '
a22 = '  '
a23 = '  '
a31 = '  '
a32 = '  '
a33 = '  '

b11 = '  '
b12 = '  '
b13 = '  '
b21 = '  '
b22 = '  '
b23 = '  '
b31 = '  '
b32 = '  '
b33 = '  '

# STAR OF THE GAME

# presenting the game
print('Welcome to Duel 52\n')
sleep(0.5)
print('This game was created by Judd Madden and Nina Riddell.\n')
sleep(0.3)
print("And I'm trying to make their game on Python :D\n")
sleep(0.3)
print('Enjoy\n')
sleep(0.5)
print('.')
print('.')
print('.\n')

# show game board to the players
print("I'm going to display your face down cards for you.\n")
sleep(0.5)
# '??' represents the face_down cards
game_board(a01='??',a02='??',a03='??',a11='  ',a12='  ',a13='  ',a21='  ',a22='  ',a23='  ',a31='  ',a32='  ',a33='  ',
b01='??',b02='??',b03='??',b11='  ',b12='  ',b13='  ',b21='  ',b22='  ',b23='  ',b31='  ',b32='  ',b33='  ') 

sleep(0.5)

# show player1 hand
print('Player 1 starts the game.\n')
sleep(0.3)
print('This is Player 1 hand:')
print(show_cards(hand_player1))

print('Draw a card')
# draw a card when the turn starts
draw_pile, card, end_game = draw_card(draw_pile,end_game)
hand_player1 = hand_player1 + [card]
print(show_cards(hand_player1))

# give the options to the player

print('You can use three actions. What do you want to do?')






