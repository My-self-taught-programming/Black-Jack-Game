import time

suits = ("♠", "♣", "♥", "♦")
ranks = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10,
          "ACE": 11, }

import random
import pyfiglet
banner = pyfiglet.figlet_format("♠ ♣ BLACKJACK ♥ ♦")


# classes
playing = True


# card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (f"--------"  
                        f"\n|{self.rank}       |"
                        f"\n|        |"
                        f"\n|   {self.suit}    |"
                        f"\n|        |"
                        f"\n|      {self.rank} |"
                        f"\n --------"   )
        # return f"{self.rank} of {self.suit}"


# deck
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return f"the deck has: {deck_comp}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "ACE":
            self.aces += 1





    def adjust_for_aces(self):
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1

        # fucnitons

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to hit or stand: [Hit or stand?]")

        if x[0].lower() == "h":
            hit(deck, hand)

        elif x[0].lower() == "s":
            print("Player stands, dealer is playing")
            playing = False

        else:
            print("Invlaid command please enter Hit or stand.")
            continue
        break

def show_some(player, dealer):
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])

def show_all(player, dealer):
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)

def player_wins(player, dealer):
    print("\n--- Player has blackjack! You win! ---")

def player_busts(player, dealer):
    print("\n--- Player busts! ---")

def dealer_busts(player, dealer):
    print("\n--- Dealer wins! ---")

def dealer_wins(player, dealer):
    print("\n--- Dealer wins! ---")

def push(player, dealer):
    print("\nIts a tie!")

while True:
    print(banner)
    # print("************************************************************")
    # print("*********** WELCOME TO TYLERS BLACKJACK TABLE!!! ***********")
    # print("************************************************************")
    print(
            "\n The rules of black jack is to get as close to the sum of 21\n, or 21 itself, with you cards as you can.")

    # Create & shuffle the deck, deal two cards to each
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

        # Show the cards:
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand)
            break
        # If Player hasn't busted, play Dealer's hand
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        time.sleep(1)
        print("\n----------------------------------------------------------------")
        print("                     The Results are in!")

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand)

        else:
            push(player_hand, dealer_hand)

    play_again = input("would you like to play again? [Y/N]")
    while play_again.lower() not in ["y", "n"]:
        play_again = input("Invalid Input. Please enter 'y' or 'n' ")
    if play_again[0].lower() == "y":
        playing = True
        continue
    else:
        print("\n------------------------Thanks for playing!---------------------\n")
        break

