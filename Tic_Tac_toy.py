from random import randint
from os import system

#board = [' ']*10

def clear():
	system("cls")

def players():
	p1 = input("Player 1 input your name: ")
	p2 = input("Player 2 input your name: ")
	return (p1,p2)

#player1,player2 = players()

def choose_first(player1,player2):
	if randint(0,1) == 0:
		return player1
	else:
		return player2

def display_board(board):
	clear()
	print("\n\n\n\n")
	print("{0:^8}|{1:^8}|{2:^8}".format(board[7],board[8],board[9]))
	print("{0:-^8}|{1:-^8}|{2:-^8}".format("","",""))
	print("{0:^8}|{1:^8}|{2:^8}".format(board[4],board[5],board[6]))
	print("{0:-^8}|{1:-^8}|{2:-^8}".format("","",""))
	print("{0:^8}|{1:^8}|{2:^8}".format(board[1],board[2],board[3]))

#display_board(board)

def choose_marker(player):
	choice = " "
	while choice not in ['X','O']:
		choice = input(player + " choose your marker between (X,O): ").upper()
	if(choice == 'X'):
		return ('X','O')
	else:
		return ('O','X')

#first,second = choose_marker()

def is_free(board,position):
	return board[position] == ' '

def input_position(board,name):
	position = 0
	while position not in range(1,10) or not is_free(board,position):
		position = int(input(name + " Enter position between (1-9): "))
	return position

#position = input_position(board)

def set_marker(board,position,marker):
	board[position] = marker

# set_marker(board,position,first)
# display_board(board)

def full_board_check(board):
	space = True
	for i in range(1,10):
		if board[i] == ' ':
			space = False
		else:
			pass
	return space

def play_again():
	ans = ' '
	while ans not in['Y','N']:
		ans = input("Do you want to play agin (Y/N): ").upper()
	if ans == 'Y':
		return True
	else:
		clear()
		return False

def win_check(board,marker):
	return ((board[1] == marker and board[2] == marker and board[3] == marker) or
			(board[4] == marker and board[5] == marker and board[6] == marker) or
			(board[7] == marker and board[8] == marker and board[9] == marker) or
			(board[1] == marker and board[4] == marker and board[7] == marker) or
			(board[2] == marker and board[5] == marker and board[8] == marker) or
			(board[3] == marker and board[6] == marker and board[9] == marker) or
			(board[1] == marker and board[5] == marker and board[9] == marker) or
			(board[3] == marker and board[5] == marker and board[7] == marker))

def game_logic():
	game_on = True
	
	while game_on:
		clear()
		board = [' ']*10
		#Welcome statement
		print("Welcome to game of Tic-Tac-Toe")
		
		#Take player name
		player1,player2 = players()
		
		#choose who's first
		first = ' '
		second = ' '
		if choose_first(player1,player2) == player1:
			print(player1 + " will go first")
			first = player1
			second = player2
			#choosing marker
			p1m,p2m = choose_marker(player1)
		else:
			print(player2 + " will go first")
			first = player2
			second = player1
			#choosing marker
			p1m,p2m = choose_marker(player2)
		
		#Ask for starting the game
		start = ' '
		while start not in ['Y','N']:
			start = input("Should we start the game (Y/N): ").upper()
		if start == 'Y':
			game_start = True
		else:
			game_start = False

		#displaying the board
		display_board(board)

		turn = 1
		while game_start:
			if turn % 2 != 0:
				#take position
				position = input_position(board,first)
				#place marker
				set_marker(board,position,p1m)
				#display board
				display_board(board)
				#check win_check
				if win_check(board,p1m):
					print("Hurray!!! "+first+" won.")
					game_start = False
					break
				#check full board check
				turn += 1
				if turn > 9:
					print("match draw!")
					game_start = False
					break
			else:
				#take position
				position = input_position(board,second)
				#place marker
				set_marker(board,position,p2m)
				#display board
				display_board(board)
				#check win_check
				if win_check(board,p2m):
					print("Hurray!!! "+second+" won.")
					game_start = False
					break
				#check full board check
				turn += 1

		#Ask to play again
		if play_again():
			game_on = True
		else:
			game_on = False

game_logic()