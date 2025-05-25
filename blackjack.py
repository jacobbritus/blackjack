#blackjack project
import random
import os
cards_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

figures_list = [chr(9829), chr(9830), chr(9830), chr(9827)]

HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.

def create_card(num, figure):
    split = ["┌───────┐", "│{}     │".format(str(num).ljust(2)), "│       │", "│   {}  │".format(figure.center(2)),
             "│       │", "│     {}│".format(str(num).rjust(2)), "└───────┘"]

    return split

# prints the cards side by side
def print_cards(deck):
    placeholder = ""

    for i in range(0, len(deck[0])):
        card_number = 0
        placeholder += deck[card_number][i]


        # if more cards
        while True:
            try:
                card_number += 1
                placeholder += deck[card_number][i]
            except IndexError:
                break
        placeholder += "\n"

    print(placeholder)





def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# set up
def deal_cards():
    #both the player and the computer get two random cards
    return [[random.choice(cards_list), random.choice(figures_list)] for cards in range(0,2)], [[random.choice(cards_list), random.choice(figures_list)], ["#", "#"]]




#start



#1. shows the players cards and one of computer's cards


#2. player's turn

def players_turn():
    while True:
        #computer cards
        #player cards
        hit_or_stand = input("Enter \"h\" to hit or \"s\" to stand.")
        clear_terminal()

        # hit
        if hit_or_stand == "h":
            player_deck.append([random.choice(cards_list), random.choice(figures_list)])
            print_deck(computer_deck)
            print_deck(player_deck)

            # player goes over 21
            if deck_total(player_deck) > 21:
                print("Bust.")
                input("Press \"Enter\" to continue.")
                clear_terminal()
                break

            else:
                continue
        # stand
        else:
            break



#3. computer's turn

def computers_turn():
    global computer_deck
    computer_deck.pop()
    computer_deck.append([random.choice(cards_list), random.choice(figures_list)])

    print_deck(computer_deck)
    print_deck(player_deck)
    input("Press \"Enter\" to continue.")
    clear_terminal()

    while deck_total(computer_deck) < 17:
        computer_deck.append([random.choice(cards_list), random.choice(figures_list)])
        print_deck(computer_deck)
        print_deck(player_deck)
        input("Press \"Enter\" to continue.")
        clear_terminal()

        #computer goes over 21
        if deck_total(computer_deck) > 21:
            print("Bust.")
            print("Player wins.")
            input("Press \"Enter\" to continue.")
            clear_terminal()

            break




#4. comparing totals

def comparing_totals():
    # player wins
    if deck_total(player_deck) > deck_total(computer_deck):
        print("Player wins.")
    # computer wins
    elif deck_total(computer_deck) > deck_total(player_deck):
        print("Computer wins.")
    # draw
    else:
        print("Draw.")


player_deck = []
computer_deck = []

def print_deck(deck):
    print(deck_total(deck))
    display = [create_card(deck[i][0], deck[i][1]) for i in range(0, len(deck))]
    print_cards(display)

def game():
    global player_deck, computer_deck
    while True:
        player_deck, computer_deck = deal_cards()


        print_deck(computer_deck)
        print_deck(player_deck)





        players_turn()
        if not 21 < deck_total(player_deck):
            computers_turn()
            if not 21 < deck_total(computer_deck):
                comparing_totals()


        game_over()

def deck_total(deck):
    total = sum(cards[0] if not cards[0] == "#" else 0 for cards in deck)
    return total

def over_21(deck):
    total = deck_total(deck)

    if total > 21 and any(card[0] for card in deck) == 11:
        for card in deck:
            if card[0] == 11:
                card[0] = 1


    if total > 21:
        game_over()

    return


def game_over():
    play_again = input("press \"y\" to play again or \"x\" to quit.")
    clear_terminal()

    if play_again == "y":
        return
    else:
        exit()


#calculate score and calculate total




# notes
# i finished the initial logic in 15 minutes by asking chatgpt for a flowchart.
# i told myself i needed it since i didn't know how blackjack worked.
# only i feel like i used too much guidance.
# well, it's not like i missed out on learning more so i'm fine.

# i then made everything in to different functions for clarity.

# alright so i've worked an hour on this and i must say.
# i like this, i like the game, i like thinking about how it could look.
# i like thinking about my personal customization.
# it's like i can feel my liking for coding right now.
# im feeling so good right now.

# things to add
# ascii cards display #cards_display(player_cards, computer_cards)
# i want the display to look like a turn based game with a lil menu (pokemon)
# i want a text box ad the bottom and scrolling text
# betting money and saving the amount to a file
# main menu
# stronger logic


# 23 / 05 / 2025
# i changed the cards system
# all cards get a figure
# each card is stored in a list
# each card is turned into an ascii version of it and then printed

# 24 / 05 / 2025
# the code's kind of messy, so i'll fix it now.
# primarily, with a function that prints out the decks

game()