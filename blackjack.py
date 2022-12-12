# Write your blackjack game here.
import random

SUITS = ['♣️', '♠️', '♥️', '♦️']
RANKS = ['A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


card = Card('♣️', 2)

# print(card)


class Deck:
    def __init__(self, suits, ranks):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank)
                self.cards.append(new_card)

    def __str__(self):
        deck_as_string = ''
        for card in self.cards:
            deck_as_string += f'{card.rank}{card.suit}  '
        return deck_as_string

    def shuffle(self):
        random.shuffle(self.cards)


class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()


my_deck = Deck(SUITS, RANKS)
print(my_deck)
my_deck.shuffle()
print(f'shuffling cards\n\n\n{my_deck}')

new_game = Game()

print(f'\n\n\n{new_game.deck}')
