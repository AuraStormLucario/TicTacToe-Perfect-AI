# Perfect TicTacToe AI, will never lose, programmed by Jordan Oberstein.

import random

X = "X" # define X
O = "O" # define O
empty = " " # define an empty space
S = [" "] * 9 # array of 9 spaces
turn = 1 # turn counter

def print_instructions():
	print "This is a game of Tic Tac Toe, the computer will never lose."
	print "Fill in spaces on the board according to the board printed below.\n"
	print "  1 | 2 | 3"
	print " ","-" * 9
	print "  4 | 5 | 6"
	print " ","-" * 9
	print "  7 | 8 | 9\n"
	print "If you get 3 of your leters in a row (horizontally, vertically, or diagonally), then you win!"
	print "Good luck!\n"

def print_board(): # prints board
	print "\n ",S[0],"|",S[1],"|",S[2]
	print " ","-" * 9
	print " ",S[3],"|",S[4],"|",S[5]
	print " ","-" * 9
	print " ",S[6],"|",S[7],"|",S[8],"\n"

def assign_winconditions(): # array of win conditions
	global WinConditions
	WinConditions = [
		(S[0], S[1], S[2]), # row1
		(S[3], S[4], S[5]), # row2
		(S[6], S[7], S[8]), # row3
		(S[0], S[3], S[6]), # col1
		(S[1], S[4], S[7]), # col2
		(S[2], S[5], S[8]), # col3
		(S[0], S[4], S[8]), # dia1
		(S[2], S[4], S[6]) # dia2
	]
	Corners = [0, 2, 6, 8]
	Edges = [1, 3, 5, 7]

def assign_letter(): # assigns chosen assign_letter to player
	global player, cpu
	cpu = empty
	player = raw_input('What assign_letter would you like to be: ')
	while not (player == "X" or player == "O" or player == "x" or player == "o"):
		player = raw_input('What assign_letter would you like to be: ')
	if player == X or player == 'x':
		player = X
		cpu = O
	if player == O or player == "o":
		player = O
		cpu = X

def assign_order(): # randomly chooses order of turns
	global order
	choice = random.choice('XO')
	print choice + " will go first"
	if choice == X:
		order = [" ", X, O, X, O, X, O, X, O, X]
	if choice == O:
		order = [" ", O, X, O, X, O, X, O, X, O]
	print order,"is the order."
	print player + " is the player."
	print cpu + " is the cpu."

def check_win(): # checks if there is winner
	global winner
	winner = empty
	for i in range(0, 8):
		if WinConditions[i] == (X, X, X):
			winner = "X"
			print winner + " wins using WinCondition",WinConditions[i],"index",i
		if WinConditions[i] == (O, O, O):
			winner = "O"
			print winner + " wins using WinCondition",WinConditions[i],"index",i
		i += 1

def player_move(turn): # function for player's move
	global moveP
	moveP = raw_input('Choose a Space from 1-9 for ' + player + ' to Go: ')
	while not moveP.isdigit() or int(moveP) not in range (1, 10) or S[int(moveP) - 1] is not empty:
		moveP = raw_input('Choose a Space from 1-9 for ' + player + ' to Go: ')
	S[int(moveP) - 1] = order[turn]
	print "The Player has gone on space",moveP,"index",int(moveP) - 1

def cpu_win(): # checks if cpu can win
	global movelist
	if WinConditions[0] == (empty, cpu, cpu) or WinConditions[3] == (empty, cpu, cpu) or WinConditions[6] == (empty, cpu, cpu):
		movelist.append(0)
	if WinConditions[0] == (cpu, empty, cpu) or WinConditions[4] == (empty, cpu, cpu):
		movelist.append(1)
	if WinConditions[0] == (cpu, cpu, empty) or WinConditions[5] == (empty, cpu, cpu) or WinConditions[7] == (empty, cpu, cpu):
		movelist.append(2)
	if WinConditions[1] == (empty, cpu, cpu) or WinConditions[3] == (cpu, empty, cpu):
		movelist.append(3)
	if WinConditions[1] == (cpu, empty, cpu) or WinConditions[4] == (cpu, empty, cpu) or WinConditions[6] == (cpu, empty, cpu) or WinConditions[7] == (cpu, empty, cpu):
		movelist.append(4)
	if WinConditions[1] == (cpu, cpu, empty) or WinConditions[5] == (cpu, empty, cpu):
		movelist.append(5)
	if WinConditions[2] == (empty, cpu, cpu) or WinConditions[3] == (cpu, cpu, empty) or WinConditions[7] == (cpu, cpu, empty):
		movelist.append(6)
	if WinConditions[2] == (cpu, empty, cpu) or WinConditions[4] == (cpu, cpu, empty):
		movelist.append(7)
	if WinConditions[2] == (cpu, cpu, empty) or WinConditions[5] == (cpu, cpu, empty) or WinConditions[6] == (cpu, cpu, empty):
		movelist.append(8)
	print movelist

def cpu_block(): # checks if player can win
	global movelist
	if WinConditions[0] == (empty, player, player) or WinConditions[3] == (empty, player, player) or WinConditions[6] == (empty, player, player):
		movelist.append(0)
	if WinConditions[0] == (player, empty, player) or WinConditions[4] == (empty, player, player):
		movelist.append(1)
	if WinConditions[0] == (player, player, empty) or WinConditions[5] == (empty, player, player) or WinConditions[7] == (empty, player, player):
		movelist.append(2)
	if WinConditions[1] == (empty, player, player) or WinConditions[3] == (player, empty, player):
		movelist.append(3)
	if WinConditions[1] == (player, empty, player) or WinConditions[4] == (player, empty, player) or WinConditions[6] == (player, empty, player) or WinConditions[7] == (player, empty, player):
		movelist.append(4)
	if WinConditions[1] == (player, player, empty) or WinConditions[5] == (player, empty, player):
		movelist.append(5)
	if WinConditions[2] == (empty, player, player) or WinConditions[3] == (player, player, empty) or WinConditions[7] == (player, player, empty):
		movelist.append(6)
	if WinConditions[2] == (player, empty, player) or WinConditions[4] == (player, player, empty):
		movelist.append(7)
	if WinConditions[2] == (player, player, empty) or WinConditions[5] == (player, player, empty) or WinConditions[6] == (player, player, empty):
		movelist.append(8)
	print movelist

def cpu_restrictions(): # combines previous 2 restrictions into 1 function
	global movelist
	movelist = [] # list of moves, optimal move inserted at begining
	print movelist
	cpu_win()
	print "After cpu_win",movelist
	cpu_block()
	print "After cpu_block",movelist

def cpu_move_turn_one(turn): # cpu move for turn 0, corner
	moveC = random.randint(0, 4)
	while S[moveC * 2] is not empty or moveC == 2:
		moveC = random.randint(0, 4)
	print moveC,"is random intiger"
	S[moveC * 2] = order[turn]
	print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2

def cpu_move_turn_two(turn): # cpu move for turn 1, center, if no center than corner
	moveC = 2
	while S[moveC * 2] is not empty:
		moveC = random.randint(0, 4)
	print moveC,"is random intiger"
	S[moveC * 2] = order[turn]
	print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2

def cpu_move_turn_three(turn): # cpu move for turn 2
	if (S[1] or S[3] or S[5] or S[7]) == player: # if player is edge, cpu moves in center
		S[4] = order[turn]
		print "The Computer will go on space 5 index 4"
	if (S[0] or S[2] or S[6] or S[8]) == player: # if player is corner, cpu moves in corner
		moveC = random.randint(0, 4)
		while S[moveC * 2] is not empty or moveC == 2:
			moveC = random.randint(0, 4)
		S[moveC * 2] = order[turn]
		print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2
	if S[4] == player: # if player is center, cpu moves in opposite corner from turn 0
		for moveC in range(0, 4):
			if S[moveC * 2] == cpu and S[8 - (moveC * 2)] == empty: # code block can only run once
				S[8 - (moveC * 2)] = order[turn]
				print "The Computer will go on space",9 - (moveC * 2),"index",8 - (moveC * 2)

def cpu_move_turn_four(turn):
	if player == S[4]:
		for moveC in range(0, 4):
			if S[moveC * 2] == player and S[8 - (moveC * 2)] == cpu: # player is center and corner, cpu is opposite corner
				moveC = random.randint(0, 4)
				while S[moveC * 2] is not empty or moveC == 2:
					moveC = random.randint(0, 4)
				S[moveC * 2] = order[turn]
				print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2
	elif cpu == S[4]:
		for moveC in range(0, 1):
			if S[moveC * 2] == player and S[8 - (moveC * 2)] == player: # cpu is center, player is 2 opposite corners
				moveC = random.randint(0, 3)
				while S[(moveC * 2) + 1] is not empty:
					moveC = random.randint(0, 3)
				S[(moveC * 2) + 1] = order[turn]
				print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2
	else:
		cpu_move(turn)

def cpu_move(turn): # cpu move for turns > 2
	moveC = random.randint(0, 8)
	while S[moveC] is not empty:
		moveC = random.randint(0, 8)
	print moveC,"random move, placeholder"
	cpu_restrictions()
	print movelist
	print moveC,"Final Option for Move C"
	if movelist == []:
		S[moveC] = order[turn]
		print "The Computer will go on space",moveC + 1,"index",moveC
	else:
		moveC = movelist[0]
		S[int(moveC)] = order[turn]
		print "The Computer will go on space",int(moveC) + 1,"index",moveC

def main(turn): # combines function into complete game
	print_instructions()
	assign_letter()
	assign_order()
	print_board()
	assign_winconditions()
	while turn < 10: # gameplay runs in this loop
		print "turn:",turn
		if order[turn] == player:
			player_move(turn)
		if order[turn] == cpu:
			if turn == 1:
				cpu_move_turn_one(turn)
			if turn == 2:
				cpu_move_turn_two(turn)
			if turn == 3:
				cpu_move_turn_three(turn)
			if turn == 4:
				cpu_move_turn_four(turn)
			if turn > 4:
				cpu_move(turn)
		print_board()
		assign_winconditions()
		check_win()
		turn += 1
		if winner is not empty:
			turn = 10
			print winner + " Is tne Winner!\n"
		if winner is empty and turn == 10:
			print "The Game Is a Tie.\n"

main(turn)

''' 
Issues:
- Add function to recognize move that makes fork
- Add cpu_move_turn_four()
- Try to eliminate global variables
- Simplify Functions]
	- assign_letter()
	- cpu_win()
	- cpu_block()
	- main(turn)
- Make order[turn] and player/cpu consistent

Stylizing (https://www.python.org/dev/peps/pep-0008/#introduction):
- Change tabs to 4 spaces
- Make all lines < 80 characters (comments < 72)
'''

'''
player plays corner
	cpu plays center
		player plays opposite corner (to player)
			cpu plays any edge							case
		player plays adjacent corner (to player)
			cpu plays edge between player corners		case (check_win)
		player plays opposite edge (to player)

		player plays adjacent edge (to player)

player plays edge
	cpu plays center
		player plays opposite corner (to player)
			cpu plays adjacent corner (to player)
		player plays adjacent corner (to player)
			cpu plays corner blocking cpu				check_win
		player plays opposite edge (to player)

		player plays adjacent edge (to player)


player plays center
	cpu plays corner 
		player plays opposite corner (to cpu)
			cpu plays corners							case
		player plays adjacent corner (to cpu)
			cpu plays empty adjacent corner (to cpu)	check_win
		player plays opposite edge (to cpu)

		player plays adjacent edge (to cpu)

cpu plays corner
	player plays corner
		cpu plays corner
	player plays opposite edge (to cpu)
		cpu plays center
	player plays adjacent edge (to cpu)
		cpu plays center
			EXTRA
			player plays opposite corner (to cpu) blocks win
				cpu plays empty adjacent edge (to cpu)
	player plays center
		cpu plays opposite corner (to cpu)
'''
