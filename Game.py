# all allow game to function
# comparison functions, player updaters, run a game, lists of information about each game.
# basic raises by AI players
import random
from Deck import Deck
from Player import Player

class Game:
    def __init__(self,Allplayers):
        self.numPlayers = len(Allplayers)
        self.players = Allplayers
        self.deck = Deck().get_deck()
        self.games_played = 0

    def get_mixed(self):
        self.mixDeck = self.deck
        random.shuffle(self.mixDeck)
        return self.mixDeck

    def deal_cards(self):
        self.games_played += 1
        self.get_mixed()
        for x in range(0,self.numPlayers):
             self.players[x].give_hand(self.mixDeck[x],self.mixDeck[x+self.numPlayers])
        del self.mixDeck[0:(self.numPlayers*2)]


    def get_players(self):
        return self.players

    def make_community(self):
        self.ccard = []
        self.ccard[0:3] = self.mixDeck[0:3]
        self.ccard.append(self.mixDeck[4])
        self.ccard.append(self.mixDeck[6])
        del self.mixDeck[0:7]
        return self.ccard










