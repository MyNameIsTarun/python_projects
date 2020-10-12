#Globals and imports
import random

suits = ('Diamonds','Hearts','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


#Card Class
class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank+" of "+self.suit

two_of_spades = Card('Spades','Two')
ace_of_diamond = Card('Diamonds','Ace')


#Deck Class
class Deck:
	def __init__(self):
		self.all_cards = []
		#population deck class object with all the 52 cards
		for suit in suits:
			for rank in ranks:
				self.all_cards.append(Card(suit,rank))

	#function to shuffle the deck
	def shuffle(self):
		random.shuffle(self.all_cards)

	#function to pop out one card from the deck
	def deal_one(self):
		return self.all_cards.pop()

#Player class
class Player:
	def __init__(self,name):
		self.name = name

		#cards in the hand of player
		self.all_cards = []

	#remove one card from the top of all_cards and return it
	def remove_one(self):
		return self.all_cards.pop(0)

	#add cards to all_cards at the end
	def add_cards(self,cards):
		if type(cards) == type([]):
			self.all_cards.extend(cards)
		else:
			self.all_cards.append(cards)

	def __str__(self):
		return f'{self.name} has {len(self.all_cards)} cards'

#Actual Game Logic
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for _ in range(26):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())

game_on = True
round = 0

while game_on:
	round += 1
	print(f'Round: {round}')

	if(len(player_one.all_cards) == 0):
		print('Player One out of cards! Player two wins')
		game_on = False
		break

	if(len(player_two.all_cards) == 0):
		print('Player Two out of cards! Player one wins')
		game_on = False
		break

	player_one_cards = []
	player_one_cards.append(player_one.remove_one())

	player_two_cards = []
	player_two_cards.append(player_two.remove_one())

	at_war = True
	#at war
	while at_war:
		if player_one_cards[-1].value > player_two_cards[-1].value:
			player_one.add_cards(player_one_cards)
			player_one.add_cards(player_two_cards)
			at_war = False
			break

		elif player_one_cards[-1].value < player_two_cards[-1].value:
			player_two.add_cards(player_two_cards)
			player_two.add_cards(player_one_cards)
			at_war = False
			break

		else:
			print('War!')

			#when both the cards value is same
			#both the player draw 5 cards
			#then again at_war
			if len(player_one.all_cards) < 5:
				print('Player One unable to declare War')
				print('Player Two wins.')
				game_on = False
				break

			elif len(player_two.all_cards) < 5:
				print('Player Two unable to declare War')
				print('Player One wins.')
				game_on = False
				break

			else:
				for _ in range(5):
					player_one_cards.append(player_one.remove_one())
					player_two_cards.append(player_two.remove_one())