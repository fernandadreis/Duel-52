from lanes import game_board
from deck import make_deck, pick_a_card, show_cards
deck = make_deck() # the deck of this game

# START OF THE GAME
print('Welcome to Duel 52')
# dealing cards
face_down = deck[0:6] # 1 face_down card in each lane for each player

# each player starts with 5 cards on hand
hand_player1 = deck[6:11] 
hand_player2 = deck[11:16]

draw_pile = deck[16:42] # 10 cards are removed from the deck, so the draw_pile has 26 cards

hand = show_cards(hand_player1)
print(hand)

