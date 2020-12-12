from collections import namedtuple
from itertools import product
import random


def make_deck():
    ''' () -> list
    Create a shuffled deck with 42 cards (13 ranks and 4 suits) 
    '''

    Card = namedtuple('Card', ['rank', 'suit'])

    ranks = {'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'}
    suits = {'♥', '♠', '♦', '♣'}

    deck = [Card(rank, suit) for rank, suit in product(ranks, suits)]
    random.shuffle(deck)

    return deck

def pick_a_card(deck, position):
    card = deck[position]
    return (card.rank, card.suit)

def show_cards(hand):
    ''' (list) -> str
    Print a list of cards
    '''
    print_hand = ''
    for i in range(len(hand)):
        rank, suit = pick_a_card(hand,i)
        print_hand += rank
        print_hand += suit
        print_hand += '  ' 
    return print_hand

