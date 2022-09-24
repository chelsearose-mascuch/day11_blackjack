#the below logo came form art.py
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

# Below is the game launcher, it asks if the user wants to play a game
#  and either bids the user farewell, or prints the new game screen and
#  launches run_blackjack(). It then returns a boolean value based on the
#  last user input to either quit or play another round
def game_launcher():
    import os
    print("")
    play=input('Do you want to play a game of Blackjack? y/n: ')
    if play == 'n':
        print("")
        print('Goodbye!')
        print("")
        return False
    else:
        os.system('clear')
        print(logo)
        run_blackjack()
        return True

# The below returns one random card out of the set of possible cards
def deal_card():
    import random
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return(card)

# The below calculates the score of the hand and repeatedly checks if any aces
#  need to be set to 1 until the score either becomes less than 21 or there are
#  no more aces left. It also checks for Blackjack and sets the score to 0 if
#  true. After revisions, it returns the final score for the hand.
def calculate_score(hand):
    loop = True
    while loop is True:
        score=sum(hand)
        if score == 21:
            score = 0
            break
        if score > 21:
            if hand.count(11) == 0:
                break
            else:
                hand.remove(11)
                hand.append(1)
                continue
        else:
            loop = False
    return score

# The below checks through the possible game outcomes and prints a message to
#  the user accordingly.
def declare_winner(dealer, player):
    if player > 21:
        print('Sorry, you went over! Better luck next time...')
    elif dealer > 21:
        print('The dealer went over! What a loser, right?')
    elif dealer == 0:
        print("Dealer has Blackjack! You lose TT_TT ")
    elif player == 0:
        print("BLACKJACK! Congrats bestie <3")
    elif player > dealer:
        print('Niiiiiiiiice!')
    elif player == dealer:
        print('A draw! GG')
    else:
        print('Wow, beaten by a computer. Sucks to be you!')

# Below is the main game console. This script runs through creating the start
#  hands, asking the player if they'd like to draw more cards (if appropriate),
#  and then finishes filling in the dealer's hand. It then prints final scores,
#  declares a winner, and asks if the user would like to keep playing.
def run_blackjack():
    dealer_hand = list()
    player_hand = list()
    for _ in range(2):
        dealer_hand.append(deal_card())
        player_hand.append(deal_card())
    gameover=False
    while gameover == False:
        dealer_score = calculate_score(dealer_hand)
        player_score = calculate_score(player_hand)
        print("")
        print("Player hand:",player_hand,"score:",player_score)
        print("Dealer card:",dealer_hand[0])
        if player_score == 0 or player_score>21:
            gameover=True
        else:
            deal = input("Would you like to draw a card? y/n: ")
            if deal == 'y':
                player_hand.append(deal_card())
            else:
                break
    while gameover == False:
        dealer_score=calculate_score(dealer_hand)
        if dealer_score==0 or dealer_score>21:
            gameover = True
            break
        if dealer_score < 17:
            dealer_hand.append(deal_card())
            continue
        else:
            gameover = True
            break
    print("")
    print('FINAL:')
    print("Player hand:",player_hand,"score:",player_score)
    print("Dealer hand:",dealer_hand,"score:",dealer_score)
    print("")
    declare_winner(dealer_score,player_score)

# This is the actual launch script. This is the first code that runs and
#  controls when to quit the game.
play = True
while play == True:
    play = game_launcher()
