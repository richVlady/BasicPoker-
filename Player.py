# Create task performance
# play poker against bots
# main file
import random
class Player:
    def __init__(self, name, money, status):  # construct player and status
        self.hand = None
        self.name = str(name)
        self.money = int(money)
        self.status = status
        self.games_won = 0
        self.avg_bet = 0
        self.points = 0
        self.rounds_played = 0
        self.game_bet = 0
        self.high_card = None

    def bet(self, money):
        self.curbet = money
        self.avg_bet += money

    def change_game_bet(self,mon):
        self.game_bet = mon

    def get_game_bet(self):
        return self.game_bet

    def get_bet(self):
        return self.curbet

    def get_avg(self):
        return self.avg_bet/self.rounds_played

    def get_hand(self):
        return self.hand

    def get_name(self):
        return self.name

    def give_hand(self, c1, c2):  #give player two cards for the hand they recieved
        self.hand = [c1,c2]

    def get_money(self):
        return self.money

    def change_money(self, money,ADSUB):
        if ADSUB:
            self.money += money
        else:
            self.money -= money

        # fold all hands that are non-suited, non-faced, non-connetors.
        # compare each players hand to the community cards based on a point system
        # higher points = high bet. (A-A = all in + 10% chance of all in if 2 or more points)
    def count_points_preflop(self):
        self.rounds_played += 1
        self.points = 0
        c1 = self.hand[0]
        c2 = self.hand[1]

        randomint = random.randint(1, 10)
        if randomint <= 4:
            self.points += 1
        if c1.get_suit() == c2.get_suit():
            self.points += 2
        if c1.get_num() == c2.get_num():
            self.points += 2
        if c1.get_num() == c2.get_num() + 1 or c2.get_num() == c1.get_num() + 1:
            self.points += 1
        if c1.get_num() == 13 or c1.get_num() == 12 or c1.get_num() == 11 or c1.get_num() == 1:
            self.points += 1
        if c2.get_num() == 13 or c2.get_num() == 12 or c2.get_num() == 11 or c2.get_num() == 1:
            self.points += 1
        if c1.get_num() == 1 and c2.get_num() == 1:
            self.points += 5
        return self.points

    def get_postflop_points(self,ccards):
        c1 = self.hand[0]
        c2 = self.hand[1]
        if c1.get_num() > c2.get_num():
            self.high_card = c1.get_num()
        else:
            self.high_card = c2.get_num()
        sList = [] #create list to check for straights and find straights
        for x in ccards:
            sList.append(x.get_num())
        sList.append(c1.get_num())
        sList.append(c2.get_num())
        sList.sort()
        counter = 0
        for x in sList:
            if x == x+1:
                counter += 1
            else:
                counter == 0
            if counter == 4:
                self.high_card == x+1
                return 4
        fList = [] #create list to check for flush and add points if one is there
        for x in ccards:
            fList.append(x.get_suit())
        fList.append(c1.get_suit())
        fList.append(c2.get_suit())
        fList.sort()
        if fList[0] == fList[4]:
            return 5
        #assign points for all other possiblities, (pair, two pair, trips)
        post_points = 0
        if c1.get_num() == c2.get_num():
            post_points += 1
        for x in ccards:
            if (c1.get_num() == x.get_num() and c2.get_num() == x.get_num()):
                post_points += 3
            elif (c1.get_num() == x.get_num()):
                post_points += 1
            elif (c2.get_num() == x.get_num()):
                post_points += 1
        return post_points


    def get_highCard(self):
        return self.high_card

    def get_points(self):
        return self.points

    def game_win(self):
        self.games_won += 1
    def update_status(self, lev):
        if lev:
            if self.status == "Master":
                return print("Master")
            if self.status == "High":
                return print("Master")
            if self.status == "Mid":
                return print("High")
            if self.status == ("Low"):
                return print("Mid")
        else:
            if self.status == "Master":
                return print("High")
            if self.status == "High":
                return print("Mid")
            if self.status == "Mid":
                return print("Low")
            if self.status == ("Low"):
                return print("Low")













