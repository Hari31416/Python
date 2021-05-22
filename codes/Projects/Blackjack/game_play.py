#Import classes
from Account import *
from Actions import *
from Card import *
from Deck import *
from Hand import *

#Introductory Lines
print("WELCOME TO BLACKJACK!")
print('The goal is to reach the hand value of 21 without passing it. Ace counts for either 1 or 11.')

#Start the game
game = Actions()
game_on = game.start_play()
while game_on:
    
    #Ask for balance to creat a player account
    balance = game.ask_balance()
    player_account = Account(balance)
    
    #Ask for bet and debit it from the player account
    #Keep asking if bet is greater than balance
    flage = True
    while flage:
        bet = game.ask_bet()
        flage = player_account.debit(bet)
        
    #Creating the deck
    deck = Deck()
    #Shuffling the deck
    deck.shuffle()
    
    #Creating hands
    player_hand = Hand()
    dealer_hand = Hand()
    
    #Passing cards to the Player
    player_hand.add_to_hand()
    print("\tPlayer")
    player_hand.add_to_hand()
    print("\tPlayer")
    
    #Passing cards to the Dealer
    dealer_hand.add_to_hand()
    print("\tDealer")
    dealer_hand.add_to_hand()
    print("\tDealer")
    
    #Show player's cards
    print("\nYour cards are:")
    for card in player_hand.all_cards:
        print(card)
    #Show first of dealer's cards
    print("\nDealer's first card is:")
    print(dealer_hand.all_cards[0])
    
    #Main playing loop
    while True:
        #Ask to stand or hit
        decision = game.stand_or_hit()
        
        #If player decides to hit
        while decision == 'h':
            print("\nYou chose to hit.")
            #Adding another card
            player_hand.add_to_hand()
            print("\tPlayer")
            print(f"Your new card is {player_hand.all_cards[-1]}.")
            decision = game.stand_or_hit()
            
        
        #If player decides to stand
        if decision == 's':
            print("You chose to stand.")
            print(f"\nDealer's second card is")
            
            # Show dealer's second card
            print(dealer_hand.all_cards[1])
            
            #count number of Aces for player
            count_ace_pl = 0
            for card in player_hand.all_cards:
                if card.rank == 'Ace':
                    count_ace_pl += 1

            #Ask for Ace adjustment
            if count_ace_pl != 0:
                print(f"You have {count_ace_pl} Ace cards.")
                adjust = game.adjust_ace()
            else:
                adjust = False

            #Chose which hand value to show depending on Ace adjustment
            if adjust:
                player_show_hand = player_hand.adjust_for_ace()
                count_ace_pl -= 1
            else:
                player_show_hand = player_hand.value_hand()

            
            #Show hand values
            print(f"Your hand value is {player_show_hand}.")            
            
            # Checck if the Player hass already lost
            if player_show_hand >= 21:
                print("You Bust. \nYou Lose!")
                player_account.debit(bet)
                break
                
                
            #If Dealer's hand value is less than 17 keep drawing cards
            flage = True
            while flage:
                #set Ace counter for dealer
                count_ace_dl = 0
                for card in dealer_hand.all_cards:
                    if card.rank == 'Ace':
                        count_ace_dl += 1
                
                print(f"Dealer has {count_ace_dl} Ace card.")
                #Ace adjustment for dealer
                if count_ace_dl != 0 and dealer_hand.value_hand()>=21:
                    adjust = True
                    count_ace_dl -= 1
                else:
                    adjust = False

                #Chose which hand value to show depending on Ace adjustment
                if adjust:
                    dealer_show_hand = dealer_hand.adjust_for_ace()
                else:
                    dealer_show_hand = dealer_hand.value_hand() 
                    
                if dealer_show_hand<17:
                    dealer_hand.add_to_hand()
                    print("\tDealer")
                    print(f"The new card is {dealer_hand.all_cards[-1]}.")
                else:
                    flage = False
                    break
            
            #Check who wins
            print(f"Dealer's final hand value is {dealer_show_hand}.")
            
            #Dealer busts
            if dealer_show_hand>=21:
                print("\nDealer Busts. You won!")
                print(f"An amount of {bet*2} chips has been credited to your account.")
                #Adding two times the bet money into player's account
                player_account.credit(bet*2)
            
            #Player loses for lesser hand
            elif player_show_hand<dealer_show_hand:
                print("You Lose!")
                print(f"Your current chip balance is {player_account.balance}")
                break
                
            #Player won because of higher hand and less than 21
            elif player_show_hand>dealer_show_hand:
                print("You Won!")
                print(f"An amount of {bet*2} chips credited to your account.")
                #Adding two times the bet money into player's account
                player_account.credit(bet*2)
                
            #Same hand value, draw
            elif player_show_hand == dealer_show_hand:
                print("Its a draw!")
                print(f"An amount of {bet} chips has been credited to your account.")
                #Adding two times the bet money into player's account
                player_account.credit(bet)
                break

        break
    game_on = game.ask_replay()
    if game_on == True:
        continue
    else:
        print("Thank you for playing Blackjack!")
        break
