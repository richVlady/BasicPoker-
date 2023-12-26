# Card file
# create and object for each card allowing easy comparisons to be made

class Card:
    # creates all cards according to give parameters
    def __init__(self, Asuit, num):
        self.number = num

        if num == 1:
            self.disnumber = "Ace"
        elif num == 11:
            self.disnumber = "Jack"
        elif num == 12:
            self.disnumber = "Queen"
        elif num == 13:
            self.disnumber = "King"
        else:
            self.disnumber = num

        if Asuit == 0:
            self.suit = "Heart"
        elif Asuit == 1:
            self.suit = "Diamond"
        elif Asuit == 2:
            self.suit = "Spade"
        else:
            self.suit = "Club"

    def get_suit(self):
        return self.suit

    def get_num(self):
        return self.number

    def get_num_display(self):
        return self.disnumber

    def get_card(self):
        return str(self.suit) + " of " + str(self.disnumber)
