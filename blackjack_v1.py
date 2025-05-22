#blackjack project
import random
import os
cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

# set up
def deal_cards():
    #both the player and the computer get two random cards
    return [random.choice(cards_list) for i in range(0, 2)], [random.choice(cards_list) for i in range(0, 2)]



#start



#1. shows the players cards and one of computer's cards


#2. player's turn

def players_turn():
    while True:
        hit_or_stand = input("Enter \"h\" to hit or \"s\" to stand.")
        clear_terminal()

        # hit
        if hit_or_stand == "h":
            player_cards.append(random.choice(cards_list))
            print(f"Your cards: {player_cards}")

            # player goes over 21
            if sum(player_cards) > 21:
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
    print(f"Computer's cards: {computer_cards}")
    input("Press \"Enter\" to continue.")
    clear_terminal()

    while sum(computer_cards) < 17:
        print("Computer hits.")
        computer_cards.append(random.choice(cards_list))
        print(f"Computer's cards: {computer_cards}")
        input("Press \"Enter\" to continue.")
        clear_terminal()

        #computer goes over 21
        if sum(computer_cards) > 21:
            print("Bust.")
            print("Player wins.")
            input("Press \"Enter\" to continue.")
            clear_terminal()

            break




#4. comparing totals

def comparing_totals():
    # player wins
    if sum(player_cards) > sum(computer_cards):
        print("Player wins.")
    # computer wins
    elif sum(computer_cards) > sum(player_cards):
        print("Computer wins.")
    # draw
    else:
        print("Draw.")


player_cards = []
computer_cards = []

def game():
    global player_cards, computer_cards
    while True:
        player_cards, computer_cards = deal_cards()

        print(f"Your cards: {player_cards}")
        print(f"Computer's card: {computer_cards[random.randint(0, len(computer_cards) - 1)]}")

        players_turn()

        if not 21 < sum(player_cards):
            computers_turn()

            if not 21 < sum(computer_cards):
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
# i want the display to look like a turn based game with a lil menu
# betting money and saving the amount to a file
# main menu
# stronger logic


game()