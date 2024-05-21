logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
from random import randint

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

dealer_turn = False

def add_card():
    if dealer_turn is False:
        player_cards.append(cards[randint(1, len(cards) -1)])
        
        return player_cards
    
    elif dealer_turn is True:
        dealer_cards.append(cards[randint(1, len(cards) -1)])

        return dealer_cards

def check_score(cards):
    score = 0
    
    for i in cards:
        score += i

    return score


while dealer_turn is False:

    player_score = check_score(player_cards)

    if player_score > 21:
        break

    print(player_score)
    response = input("Do you want another card? (y/n): ")

    if response.lower() == 'y':
        add_card()

    elif response.lower() == 'n':
        print("You have stopped... moving on to dealer")
        dealer_turn = True
        break

while dealer_turn is True:
    if len(dealer_cards) < 2:
        add_card()
        add_card()


    if check_score(dealer_cards) < 17:
        add_card()

        dealer_score = check_score(dealer_cards)

    else:
        print(f"Dealer stops with a score of {check_score(dealer_cards)}")
        dealer_score = check_score(dealer_cards)
        break

if player_score > 21:
    print("You lose, bust!")

elif dealer_score > 21:
    print("Dealer loses, bust!")

elif player_score > dealer_score:
    print("Player wins!")

elif player_score == dealer_score:
    print("Draw!")

else:
    print("Dealer wins!")  