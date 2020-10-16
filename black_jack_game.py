#Globals and imports
import random

suits = ('Diamonds','Hearts','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True

#card class
class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return f'{self.rank} of {self.suit}'

#deck class
class Deck:
	def __init__(self):
		self.deck = []
		#population deck with cards
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_compo = ""
		for card in self.deck:
			deck_compo += '\n' + card.__str__()
		return "The deck has: "+deck_compo

	#shuffles the deck
	def shuffle(self):
		random.shuffle(self.deck)

	#pop single card
	def deal(self):
		return self.deck.pop()

#Hand class
class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.cards.append(card)
		self.value += card.value

		if card.rank == "Ace":
			self.aces += 1

	def adjust_for_ace(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

#chip class
class Chips:
	def __init__(self,total=100):
		self.total = total
		self.bet = 0

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet

#function for taking bet
#passing Chip object
def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips you like to bet? "))
		except:
			print("Please provide an integer!")
		else:
			if chips.bet > chips.total:
				print("Sorry, you do not have enough chips! you have {}".format(chips.total))
			else:
				break

#fuction for taking hit
def hit(deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
	global playing

	while True:
		x = input("Hit or Stand? Enter h or s: ")

		if x[0].lower() == "h":
			hit(deck,hand)
			return "h"

		elif x[0].lower() == "s":
			print("Player stands Dealers turn")
			playing = False
			return "s"

		else:
			print("Sorry, I did not understand that, Please enter h or s!")
			continue

		break

def player_busts(player,dealer,chips):
	print("\nBUST PLAYER!")
	chips.lose_bet()

def player_wins(player,dealer,chips):
	print("\nPLAYER WINS!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("\nPLAYER WINS! DEALER BUSTED!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("\nDEALER WINS!")
	chips.lose_bet()

def push():
	print("\nDealer and player tie! PUSH")

#function for showing cards
def show_some(player,dealer):
	print("DEALERS HAND: ")
	print("one card hidden!")
	print(dealer.cards[1])
	print('\n')
	print("PLAYERS HAND: ")
	for card in player.cards:
		print(card)

def show_all(player,dealer):
	print("\nDEALERS HAND: ")
	for card in dealer.cards:
		print(card)
	print('\n')
	print("PLAYERS HAND: ")
	for card in player.cards:
		print(card)

#Actual game play
while True:
	#print an opening statement

	print("WELCOME TO BLACKJACK")
	# Create $ shuffle deck,two cards each to player $ dealer
	deck = Deck()
	deck.shuffle()

	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	# set up the player's chips
	player_chips = Chips()

	#prompt the player for their bet
	take_bet(player_chips)

	# show cards (but keep one dealer card hidden)
	show_some(player_hand,dealer_hand)

	# Player is playing
	while playing:
		# prompt for player to hit or stand
		choice = hit_or_stand(deck,player_hand)

		# show cards (but keep one dealer card hidden)
		if choice != "s":
			show_some(player_hand,dealer_hand)

		#if player's hand exceeds 21, run player_bust and break out of loop
		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			break

	# if player hasn't busted play dealer's hand until dealer reaches 17
	if player_hand.value<=21:
		while dealer_hand.value < 17:
			hit(deck,dealer_hand)

		#show all cards
		show_all(player_hand,dealer_hand)

		#run different winning scenariios
		if dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)
		else:
			push()

		# Inform player of their chips total
		print("\nPlayer total chips are at: {}".format(player_chips.total))
	
	# Ask to play again
	new_game = input("\nwould you like to play another hand? y/n: ")

	if new_game[0].lower() == 'y':
		playing = True
		continue
	else:
		print("Thank you for playing!")
		break