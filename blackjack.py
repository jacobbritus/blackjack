#blackjack project
import random
import os
cards_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

figures_list = [chr(9829), chr(9830), chr(9830), chr(9827)]

HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9830)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.

def create_card(num, figure):
    split = ["┌───────┐", "│{}     │".format(str(num).ljust(2)), "│       │", "│   {}  │".format(figure.center(2)),
             "│       │", "│     {}│".format(str(num).rjust(2)), "└───────┘"]

    return split

# prints the cards side by side
def print_cards(cards):
    tgt = ""

    for i in range(0, len(cards[0])):
        card_number = 0
        tgt += cards[card_number][i]


        # if more cards
        while True:
            try:
                card_number += 1
                tgt += cards[card_number][i]
            except IndexError:
                break
        tgt += "\n"

    print(tgt)





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
            player_cards_numbers.append([random.choice(cards_list), random.choice(figures_list)])
            print(f"You: {sum(cards[0] for cards in player_cards_numbers)}")
            player_cards_display = [create_card(player_cards_numbers[i][0], player_cards_numbers[i][1]) for i in
                                    range(0, len(player_cards_numbers))]
            print_cards(player_cards_display)

            # player goes over 21
            if sum(cards[0] for cards in player_cards_numbers) > 21:
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
    global computer_cards_numbers
    computer_cards_numbers.pop()
    computer_cards_numbers.append([random.choice(cards_list), random.choice(figures_list)])

    print(f"Dealer: {sum(cards[0] if not cards[0] == "#" else 0 for cards in computer_cards_numbers)}")
    computer_cards_display = [create_card(computer_cards_numbers[i][0], computer_cards_numbers[i][1]) for i in
                              range(0, len(computer_cards_numbers))]
    print_cards(computer_cards_display)
    input("Press \"Enter\" to continue.")
    clear_terminal()

    while sum(cards[0] for cards in computer_cards_numbers) < 17:
        print("Computer hits.")
        computer_cards_numbers.append([random.choice(cards_list), random.choice(figures_list)])
        print(f"Dealer: {sum(cards[0] if not cards[0] == "#" else 0 for cards in computer_cards_numbers)}")
        computer_cards_display = [create_card(computer_cards_numbers[i][0], computer_cards_numbers[i][1]) for i in
                                  range(0, len(computer_cards_numbers))]
        print_cards(computer_cards_display)
        input("Press \"Enter\" to continue.")
        clear_terminal()

        #computer goes over 21
        if sum(cards[0] for cards in computer_cards_numbers) > 21:
            print("Bust.")
            print("Player wins.")
            input("Press \"Enter\" to continue.")
            clear_terminal()

            break




#4. comparing totals

def comparing_totals():
    # player wins
    if sum(cards[0] for cards in player_cards_numbers) > sum(cards[0] for cards in computer_cards_numbers):
        print("Player wins.")
    # computer wins
    elif sum(cards[0] for cards in computer_cards_numbers) > sum(cards[0] for cards in player_cards_numbers):
        print("Computer wins.")
    # draw
    else:
        print("Draw.")


player_cards_numbers = []
computer_cards_numbers = []

def print_deck(deck):
    ...

def game():
    global player_cards_numbers, computer_cards_numbers
    while True:
        player_cards_numbers, computer_cards_numbers = deal_cards()

        print(f"Dealer: {sum(cards[0] if not cards[0] == "#" else 0 for cards in computer_cards_numbers)}")
        computer_cards_display = [create_card(computer_cards_numbers[i][0], computer_cards_numbers[i][1]) for i in
                                  range(0, len(computer_cards_numbers))]
        print_cards(computer_cards_display)

        print(f"You: {sum(cards[0] for cards in player_cards_numbers)}")
        player_cards_display = [create_card(player_cards_numbers[i][0], player_cards_numbers[i][1]) for i in
                                range(0, len(player_cards_numbers))]
        print_cards(player_cards_display)





        players_turn()
        if not 21 < sum(cards[0] for cards in player_cards_numbers):
            computers_turn()
            if not 21 < sum(cards[0] if not cards[0] == "#" else 0 for cards in computer_cards_numbers):
                comparing_totals()


        play_again = input("press \"y\" to play again or \"x\" to quit.")
        clear_terminal()

        if play_again == "y":
            continue
        else:
            break


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
# each card is turned into a ascii version of it and then printed

# 24 / 05 / 2025
# the code's kind of a mess, so i'll fix it now.

game()