############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The dealer is the dealer.

#import statements
from art import logo
from clear import clear
import random

#constants
print(logo)


#data
ideal_deck = [10,10,10,10,9,8,7,6,5,4,3,2,11]
player_deck = []
dealer_deck = []


#playing condition
playing_rn = True

#function definitions
#Function1: to check the overflow or bust of any deck
def bust(deck):
    if sum(deck)>21:
        return True
    else:
        return False

#Function2: to add new value to  deck
def add_to_deck(deck):
    deck.append(ideal_deck [random.randint(0,12)])
    
#Function3: to compare the user and dealer deck
def compare():
    while sum(dealer_deck) < 16:
        add_to_deck(dealer_deck)
        print(f"The dealer deck is: {dealer_deck}")
    if not bust(dealer_deck) and not bust(player_deck):
        if sum(player_deck) < sum(dealer_deck):
            return f"Dealer won as your deck: {player_deck} (whose sum is {sum(player_deck)}) and dealer deck: {dealer_deck} (whose sum is {sum(dealer_deck)})"
        elif sum(player_deck) > sum(dealer_deck):
            return f"You won as your deck: {player_deck} (whose sum is {sum(player_deck)}) and dealer deck: {dealer_deck} (whose sum is {sum(dealer_deck)})"
        elif sum(player_deck) == sum(dealer_deck):
            return "Oops, match draw"
    elif bust(dealer_deck):
        return f"Dealer got busted as his deck is {dealer_deck} whose sum is {sum(dealer_deck)}. Hence, You won"
        
start = input("Welcome to the game of black jack. Hit enter to start ! ")

if start=="":
    print("Game is starting...")
    
    #initialising dealer deck 
    add_to_deck(deck = dealer_deck)
    dealer_deck.append("hidden")
 
    #initialising user deck   
    add_to_deck(deck = player_deck)
    add_to_deck(deck = player_deck)
    if bust(player_deck):
        print(f"You got busted as your deck is {player_deck} whose sum is {sum(player_deck)}")
        quit()
    elif sum(player_deck) == 21:
        print(f"You won as your deck: {player_deck} (whose sum is {sum(player_deck)})")
    while playing_rn:
        #showing output for user to compare
        print(f"Your deck contains following cards {player_deck} which sum up to be {sum(player_deck)}. ")
        print(f"While the dealer deck contains: {dealer_deck}. ")
        choice = input("Type stand or hit ?\n").lower()
        if choice == "stand":
            #I have to initialise this so that the hidden string is removed
            dealer_deck[1] = ideal_deck[random.randint(0,12)]
            result = compare()
            print(result)
            quit()
        elif choice == "hit":
            add_to_deck(deck = player_deck)
            if bust(player_deck):
                print(f"You got busted as your deck is {player_deck} whose sum is {sum(player_deck)}, Hence, Dealer Won")
                quit()
        
else:
    print("Exiting...")
    