# run the game
# track betting, winners, update variables, and allow user influence

import names
from Game import Game
from Player import Player
# give information about the program
print("Poker simulator:")
print("This program will allow you to play a simulated poker games against a max of 5 bots")
print("Rules as followed:"
      "\n  1. Bet on preflop, and river only."
      "\n  2. You lead betting each time."
      "\n  3. Split pot on ties, otherwise winner takes full pot"
      "\n  4. End message if you bust."
      "\n  5. Enjoy!!")

# collect data from user to create players, and their own profile
userName = input("What is your name?:")
while True:
    userMoney = input("How much money would you like to buy-in with?:")
    if int(userMoney) > 0:
        break
while True:
    numPlayers = input("How many players would you like to play against (1-5)?:")
    if int(numPlayers) < 6:
        break

# create list of all players including user and number of random players
fulltable = []
user = Player(userName,int(userMoney), "Mid")
fulltable.append(user)
for numyy in range (1, int(numPlayers)+1):
    fulltable.append(Player(names.get_first_name(),int(userMoney), "Mid")) #names is an external library to supply a random names provided by Trey Hunter

#start a hand, play out the cards
start: str = input("Say \"start\" to deal cards.")
while start == "start":
    table = fulltable.copy()
    game = Game(table)
    game.deal_cards()
    ccards = []
    ccards = game.make_community()

    #print and begin to play out the hand. contains comparison calls and formatting.
    print("\n\nYour cards are:")
    c1 = table[0].get_hand()[0]
    c2 = table[0].get_hand()[1]
    print(table[0].get_name() + ": " + c1.get_card() + ", " + c2.get_card())
    bet = int(input("How much would you like to bet? (0 for fold):"))
    while True:
        if (bet == 0):
            start = input("Say \"start\" to begin a new round!")
            break
        elif bet > table[0].get_money():
            print("You do not have enough money for this bet. Bet again!")
            bet = int(input("How much would you like to bet? (0 for fold):"))
        else:
            table[0].bet(bet)
            pot = bet
            table[0].change_money(bet,False)
            #for loop to get points and determine auto bets.
            noCtable = table.copy()
            for x in noCtable:
                if x.get_name() == userName:
                    continue
                points = x.count_points_preflop()
                if points == 0:
                    print(x.get_name() + " has bet " + "0")
                    table.remove(x)
                elif points >= 1:
                    x.bet(bet)
                    pot += bet
                    x.change_game_bet(bet)
                    x.change_money(bet,False)
                    print(x.get_name() + " has bet " + str(bet))
                elif points >= 2:
                    x.bet(bet*1.5)
                    pot += bet*1.5
                    x.change_game_bet(bet*1.5)
                    x.change_money(bet*1.5, False)
                    print(x.get_name() + " has bet " + str(bet*1.5))
                elif points >= 3:
                    x.bet(bet*2)
                    pot += bet*2
                    x.change_game_bet(bet*2)
                    x.change_money(bet*2, False)
                    print(x.get_name() + " has bet " + str(bet*2))
                else:
                    x.bet(x.get_money())
                    pot += x.get_money()
                    x.change_game_bet(x.get_money())
                    x.change_money(x.get_money(), False)
                    print(x.get_name() + " has bet " + str(x.get_money()) + "(All IN)")

            print("\nCommunity Cards:")
            print("-",end='')
            for x in ccards:
                print("-" + x.get_card() + "--",end='')
            print("\nPot: " + str(pot))
            resp = int(input("Would you like to bet more? (-1 to fold, 0 to check)"))
            if resp == -1:
                start = input("Say \"start\" to begin a new round!")
                break
            table[0].change_money(resp,False)
            pot += resp

            loopertable = table.copy()
            for x in loopertable:
                if x.get_name() == userName:
                    continue
                if x.get_postflop_points(ccards) >= 1:
                    juice = (bet+resp)-(x.get_game_bet()+resp)
                    if juice >= 0:
                        pot += resp+juice
                        x.change_money(resp+juice, False)
                        x.change_game_bet(resp+bet)
                        print(x.get_name() + " has called: $" + str(x.get_game_bet()))
                    else:
                        print(x.get_name() + " has called: $" + str(x.get_game_bet()))
                else:
                    print(x.get_name() + " has folded.")
                    table.remove(x)
                currHighP = 0
                round_winner = []
            for x in table:
                print(x.get_name() + " has PFP of: ", end='')
                print(str(x.get_postflop_points(ccards)),end='')
                print(" -- " + x.get_hand()[0].get_card() + " & " + x.get_hand()[1].get_card())
                if currHighP == x.get_postflop_points(ccards):
                    round_winner.append(x)
                elif currHighP < x.get_postflop_points(ccards):
                    currHighP = x.get_postflop_points(ccards)
                    round_winner.clear()
                    round_winner.append(x)

            hCard = 0
            superWinner = []
            if len(round_winner) > 1:
                for x in round_winner:
                    if (x.get_highCard() > hCard):
                        superWinner.clear()
                        superWinner.append(x)
                    elif (x.get_highCard() == hCard):
                        superWinner.append(x)
            else:
                superWinner.append(round_winner[0])

            if len(superWinner) > 1:
                print("The pot is split between " + superWinner[0].get_name() + " and " + superWinner[1].get_name())
                superWinner[0].change_money(pot/2,True)
                superWinner[1].change_money(pot/2,True)
            else:
                print("The winner is " + superWinner[0].get_name() + ": +$" + str(pot))
                superWinner[0].change_money(pot,True)

            print("Your new balence is $" + str(table[0].get_money()))
            if table[0].get_money() < 0:
                print("You're in dept!! Ouch")
                break
            if table[0].get_money() <= 0:
                start = "BUST"
                break
            start = input("Say \"start\" to begin a new round!")
            break






