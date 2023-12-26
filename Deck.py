# DecK of cards file
# Create a functional deck of cards that can be used in the Main game class
from Card import Card

# creates a list of a full deck of cards
class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(0,4):
            for num in range(1,14):
                self.deck.append(Card(suit, num))

    def get_deck(self):
        return self.deck

#deck = Deck()
#print(deck.get_deck()[51].get_card())