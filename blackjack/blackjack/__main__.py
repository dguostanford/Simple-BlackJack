#General overview of this game:
from terminal_playing_cards import Deck, View
from blackjack.roles import Role
import random

def player_hit():
    print("*Hit Me!*")
    EX_PLAYER.hit(card=DECK.pop())
    #print(f"Your current total is {EX_PLAYER.total}")

def should_play(difficulty, COMPUTER_PLAYER, play):
    if difficulty == "1":
        if play:
            COMPUTER_PLAYER.hit(card=DECK.pop())
            if COMPUTER_PLAYER.total >= 16:
                play is False
    if difficulty == "2":
        if len(EX_PLAYER.hand) < 4 and COMPUTER_PLAYER.total <= 12:
            COMPUTER_PLAYER.hit(card=DECK.pop())
        else: 
            play is False
    if difficulty == "3":
        if EX_PLAYER.total >= 10 and COMPUTER_PLAYER.total >= 16: #computer is ahead
            play is False
        if COMPUTER_PLAYER.total + 6 <= EX_PLAYER.total:
            COMPUTER_PLAYER.hit(card=DECK.pop())

print("*This is a Simple Game of BlackJack. Single-Player Only*")

DECK = Deck(specifications=["face_cards_are_ten"])
HIDDEN_DECK = Deck(hidden=True, picture=False)
DECK.shuffle()
HIDDEN_DECK.shuffle()

difficulty = input("\n Please Select Your Difficulty Level - Beginner (1), Intermediate (2), or Advanced (3): ")
if difficulty is not '1' and difficulty is not '2' and difficulty is not '3':
    while difficulty is not "1" and difficulty is not "2" and difficulty is not "3":
        difficulty = input("\n Please Enter in a Valid Answer. Please Select Your Difficulty Level - Beginner (1), Intermediate (2), or Advanced (3): ")

EX_PLAYER = Role(hand=View(
    [DECK.pop() for _ in range(2)],
    spacing = -5
    ))
COMPUTER_PLAYER = Role(hand=View(
    [HIDDEN_DECK.pop() for _ in range (2)],
    spacing = -5
    ))

stand = False


while EX_PLAYER.total < 21 and COMPUTER_PLAYER.total < 21:
    #initialization of the game. house shows one card up, one card down. only computer knows that
    #my hand. show all of your cards

    #COMPUTER_PLAYER.hidden = False
    # if computers:

    play = True

    print("Computer's Hand: ")
    print(COMPUTER_PLAYER.hand)
        
    print("Your Hand: ")
    print(EX_PLAYER.hand)

    should_play(difficulty, COMPUTER_PLAYER, play)

    #your hand
    val = input("Enter 's' to Stand or 'h' to hit: ")#initial option to stay or hit
    if val == "h" or val == "hit" or val == "Hit":
        player_hit()
    if val == "s" or val == "stand" or val == "Stand":#if you stay, you automatically forfeit game 
        if stand is True:
            break
        stand is True


#Game outcomes:

if EX_PLAYER.total == 21:
    print(f"Congratulations! You Got 21.")
    print(f"Your Final Hand of {EX_PLAYER.total} is as such:")

#if you have less than or more than 21, have to compare with the computers hand
if EX_PLAYER.total > 21:
    print(f"Your Final Hand of {EX_PLAYER.total} is as such:")

if EX_PLAYER.total < 21:
    print(f"Your Final Hand of {EX_PLAYER.total} is as such:")
    if EX_PLAYER.total > COMPUTER_PLAYER.total:
        print(f"Congratulations! You had the highest total!")
    if COMPUTER_PLAYER.total > EX_PLAYER.total and COMPUTER_PLAYER.total <= 21:
        print(f"Sorry, you lost. The highest total was {COMPUTER_PLAYER.total}")#change this for multiple players
    if COMPUTER_PLAYER.total > EX_PLAYER.total and COMPUTER_PLAYER.total > 21:
        print(f"Congratulations! You had the highest total!")
    if COMPUTER_PLAYER.total == EX_PLAYER.total:
        print(f"There was a tie! The Computer wins.")

print(EX_PLAYER.hand)
COMPUTER_PLAYER.hidden = False
final_hand = View([HIDDEN_DECK.pop() for _ in range(len(COMPUTER_PLAYER.hand))],
    spacing = -5,
    )
for card in final_hand:
    card.hidden = False
    new_hand = View([card],
    spacing = -5
    )
print(new_hand)