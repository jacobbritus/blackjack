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

players_cards = card(10, SPADES), card(5, CLUBS), card(2, HEARTS), card(7, DIAMONDS)
computer_cards = card(random.choice(cards_list), random.choice(figures_list)), card("#", "#")

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




print(players_cards)


display_cards(computer_cards)
display_cards(players_cards)
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

