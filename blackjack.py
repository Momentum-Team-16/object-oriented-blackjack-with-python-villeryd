# Write your blackjack game here.
import random

SUITS = ['♣️', '♠️', '♥️', '♦️']
RANKS = ['A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10]


class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank}{self.suit}    '


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
            deck_as_string += f'{card}'
        return deck_as_string

    def shuffle(self):
        random.shuffle(self.cards)


class Game:
    def __init__(self):
        self.deck = Deck(SUITS, RANKS)
        self.deck.shuffle()

    def deal_card(self, player):
        dealt_card = self.deck.cards.pop()
        player.hand.append(dealt_card)


class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        hand_as_string = ''
        for card in self.hand:
            hand_as_string += f'{card}'
            return hand_as_string


class Player:
    def __init__(self):
        self.hand = []

    def __str__(self):
        hand_as_string = ''
        for card in self.hand:
            hand_as_string += f'{card}'
            return hand_as_string


player1 = Player()
dealer = Dealer()
new_game = Game()

new_game.deal_card(player1)
new_game.deal_card(dealer)
print(player1, dealer)


print(f'\n\n\n{new_game.deck}')
