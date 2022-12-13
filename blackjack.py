# Write your blackjack game here.
import random

SUITS = ['♣️', '♠️', '♥️', '♦️']
RANKS = ['A', 'J', 'Q', 'K', 2, 3, 4, 5, 6, 7, 8, 9, 10]
FACE = ['J', 'Q', 'K']


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
        self.players = []
        self.dealer = Dealer()

    def deal_card(self, player):
        dealt_card = self.deck.cards.pop()
        player.hand.append(dealt_card)

    def deal_players(self):
        while len(self.dealer.hand) < 2:
            for player in self.players:
                self.deal_card(player)
                print(len(self.dealer.hand))

    def create_players(self):
        number = input('how many players?')
        number = int(number)
        counter = 0
        while counter < number:
            player = Player()
            player.name = f'P{counter}'
            self.players.append(player)
            counter += 1
        self.players.append(self.dealer)

    def calc_score(self, player):
        player.score = 0
        num_ace = 0
        for card in player.hand:
            if card.rank in FACE:
                player.score += 10
            elif card.rank in FACE[3:]:
                player.score += card.rank
            else:
                player.score += 11
                num_ace += 1
            while num_ace and player.score > 21:
                player.score -= 10
                num_ace -= 1


class Dealer:
    def __init__(self):
        self.hand = []
        self.name = 'Dealer'
        self.score = 0

    def __str__(self):
        return self.name

    def show_hand(self):
        hand_as_string = ''
        for card in self.hand:
            hand_as_string += f'{card}'
        return hand_as_string


class Player:
    def __init__(self):
        self.hand = []
        self.name = 'player'
        self.score = 0

    def __str__(self):
        return self.name

    def show_hand(self):
        hand_as_string = ''
        for card in self.hand:
            hand_as_string += f'{card}'
        return hand_as_string


# player1 = Player()
# dealer = Dealer()
# new_game = Game()

# new_game.deal_card(player1)
# new_game.deal_card(dealer)
# print(player1, dealer)


# print(f'\n\n\n{new_game.deck}')

new_game = Game()

new_game.create_players()
new_game.deal_players()

for player in new_game.players:
    new_game.calc_score(player)
    print(f'{player}:   {player.show_hand()} score: {player.score}')
