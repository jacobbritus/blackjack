# print(Fore.GREEN + "┌" + "─" * (BOX_LENGTH + 1) + "┐")
# print(Fore.GREEN + "│" + str(habits_list[habit]["streak"]).ljust(STREAK_TO_BOX) + "".join(
#     habits_list[habit]["marks"]).ljust(BOX_LENGTH - STREAK_TO_BOX) + "│")  # streak to be added still
# print(Fore.GREEN + "│" + habit.ljust(BOX_LENGTH + 1) + "│")
# print(Fore.GREEN + "└" + "─" * (BOX_LENGTH + 1) + "┘")
import random

cards_list = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

figures_list = [chr(9829), chr(9830), chr(9830), chr(9827)]

HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9830)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.



def card(num, figure):
    split = ["┌───────┐", "│{}     │".format(str(num).ljust(2)), "│       │", "│   {}  │".format(figure.center(2)),
             "│       │", "│     {}│".format(str(num).rjust(2)), "└───────┘"]

    return split


# prints the cards side by side
def display_cards(cards):
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



player_deck = [[random.choice(cards_list), random.choice(figures_list)] for cards in range(0, 2)]
computer_deck = [[random.choice(cards_list), random.choice(figures_list)], ["#", "#"]]


# display_cards(computer_cards)

while True:
    computer_deck = [card(computer_deck[i][0], computer_deck[i][1]) for i in range(0, len(computer_deck))]
    player_cards_display = [card(player_deck[i][0], player_deck[i][1]) for i in range(0, len(player_deck))]

    display_cards(computer_deck)
    computer_deck.append([random.choice(cards_list), random.choice(figures_list)])


    display_cards(player_cards_display)
    player_deck.append([random.choice(cards_list), random.choice(figures_list)])
    input()


# print(tgt)
#
# output = ""
# for index, show in enumerate(tgt):
#
#     output += "".join(show)
#
#     if index % 2 != 0 and not index == 0:
#         output += "\n"
#
#
# print(output)
# input()

# full = [cards[0][0], cards[1][0]]
#
# print("".join(full))

# for card in cards:
#     print("\n".join(card))
#
# input()

