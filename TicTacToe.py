# Perfect Tic Tac Toe AI, it will never lose.
# Created and programmed by Jordan Oberstein.

import random

X = "X" # define both letters
O = "O" # define both letters
empty = " " # define an empty space
S = [" ", " ", " ", " ", " ", " ", " ", " ", " "] # array of 9 spaces
turn = 0 # turn counter

def Board(): # prints board
	print "\n ",S[0],"|",S[1],"|",S[2]
	print " ","---------"
	print " ",S[3],"|",S[4],"|",S[5]
	print " ","---------"
	print " ",S[6],"|",S[7],"|",S[8],"\n"

def Instructions():
	print "This is a game of Tic Tac Toe, the computer will never lose."
	print "Fill in spaces on the board according to the board printed below.\n"
	print "  1 | 2 | 3"
	print "  ---------"
	print "  4 | 5 | 6"
	print "  ---------"
	print "  7 | 8 | 9\n"
	print "If you get 3 of your leters in a row (horizontally, vertically, or diagonally), then you win!"
	print "Good luck!\n"

def Lines(): # all win conditions
	global WinConditions, row1, row2, row3, col1, col2, col3, dia1, dia2
	row1 = (S[0], S[1], S[2])
	row2 = (S[3], S[4], S[5])
	row3 = (S[6], S[7], S[8])
	col1 = (S[0], S[3], S[6])
	col2 = (S[1], S[4], S[7])
	col3 = (S[2], S[5], S[8])
	dia1 = (S[0], S[4], S[8])
	dia2 = (S[2], S[4], S[6])
	WinConditions = [row1, row2, row3, col1, col2, col3, dia1, dia2] # array of winconditions

def Letter(): # assigns chosen letter to player
	global player, cpu
	cpu = empty
	player = raw_input('What letter would you like to be: ')
	while not (player == "X" or player == "O" or player == "x" or player == "o"):
		player = raw_input('What letter would you like to be: ')
	if player == X or player == 'x':
		player = X
		cpu = O
	if player == O or player == "o":
		player = O
		cpu = X

def WhoGoesFirst(): # randomly chooses order of turns
	global order
	Letter()
	choice = random.choice('XO')
	print choice + " will go first"
	if choice == X:
		order = [X, O, X, O, X, O, X, O, X]
	if choice == O:
		order = [O, X, O, X, O, X, O, X, O]
	print order,"is the order."
	print player + " is the player."
	print cpu + " is the cpu."

def CheckWin():
	global winner
	winner = empty
	for i in range(0, 8):
		if WinConditions[i] == (X, X, X):
			winner = "X"
			print winner + " wins using WinCondition",WinConditions[i]
		if WinConditions[i] == (O, O, O):
			winner = "O"
			print winner + " wins using WinCondition",WinConditions[i]
		i += 1

def Process(): # process of following 3 functions used at end of each turn
	Board()
	Lines()
	CheckWin()

def MovePlayer(turn): # function for player's move
	global moveP
	moveP = raw_input('Choose a Space from 1-9 for ' + player + ' to Go: ')
	while not moveP.isdigit() or int(moveP) not in range (1, 10) or S[int(moveP) - 1] is not empty:
		moveP = raw_input('Choose a Space from 1-9 for ' + player + ' to Go: ')
	S[int(moveP) - 1] = order[turn]
	print "The Player has gone on space",moveP,"index",int(moveP) - 1
	Process()

def CWin(): # checks if cpu can win
	global moveC
	print moveC
	if row1 == (empty, cpu, cpu) or col1 == (empty, cpu, cpu) or dia1 == (empty, cpu, cpu):
		moveC = 0
	if row1 == (cpu, empty, cpu) or col2 == (empty, cpu, cpu):
		moveC = 1
	if row1 == (cpu, cpu, empty) or col3 == (empty, cpu, cpu) or dia2 == (empty, cpu, cpu):
		moveC = 2
	if row2 == (empty, cpu, cpu) or col1 == (cpu, empty, cpu):
		moveC = 3
	if row2 == (cpu, empty, cpu) or col2 == (cpu, empty, cpu) or dia1 == (cpu, empty, cpu) or dia2 == (cpu, empty, cpu):
		moveC = 4
	if row2 == (cpu, cpu, empty) or col3 == (cpu, empty, cpu):
		moveC = 5
	if row3 == (empty, cpu, cpu) or col1 == (cpu, cpu, empty) or dia2 == (cpu, cpu, empty):
		moveC = 6
	if row3 == (cpu, empty, cpu) or col2 == (cpu, cpu, empty):
		moveC = 7
	if row3 == (cpu, cpu, empty) or col3 == (cpu, cpu, empty) or dia1 == (cpu, cpu, empty):
		moveC = 8

def CBlock(): # checks if player can win (blocks forks)
	global moveC, BlockFork
	print moveC
	if row1 == (empty, player, player) or col1 == (empty, player, player) or dia1 == (empty, player, player):
		moveC = 0
		BlockFork.append(moveC)
	if row1 == (player, empty, player) or col2 == (empty, player, player):
		moveC = 1
		BlockFork.append(moveC)
	if row1 == (player, player, empty) or col3 == (empty, player, player) or dia2 == (empty, player, player):
		moveC = 2
		BlockFork.append(moveC)
	if row2 == (empty, player, player) or col1 == (player, empty, player):
		moveC = 3
		BlockFork.append(moveC)
	if row2 == (player, empty, player) or col2 == (player, empty, player) or dia1 == (player, empty, player) or dia2 == (player, empty, player):
		moveC = 4
		BlockFork.append(moveC)
	if row2 == (player, player, empty) or col3 == (player, empty, player):
		moveC = 5
		BlockFork.append(moveC)
	if row3 == (empty, player, player) or col1 == (player, player, empty) or dia2 == (player, player, empty):
		moveC = 6
		BlockFork.append(moveC)
	if row3 == (player, empty, player) or col2 == (player, player, empty):
		moveC = 7
		BlockFork.append(moveC)
	if row3 == (player, player, empty) or col3 == (player, player, empty) or dia1 == (player, player, empty):
		moveC = 8
		BlockFork.append(moveC)
	print "LIST",BlockFork

def Restrict(): # combines previous 2 restrictions into 1 function
	print "Before CBlock"
	CBlock()
	print "Between CWin and CBlock"
	CWin()
	print "After CWin"

def ZEROMoveCPU(turn): # cpu move for turn 0
	moveC = random.randint(0, 4)
	while S[moveC * 2] is not empty or moveC == 2:
		moveC = random.randint(0, 4)
	print moveC,"is random intiger"
	S[moveC * 2] = order[turn]
	print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2
	Process()

def ONEMoveCPU(turn): # cpu move for turn 1
	moveC = 2
	while S[moveC * 2] is not empty:
		moveC = random.randint(0, 4)
		while S[moveC * 2] is not empty:
			moveC = random.randint(0, 4)
	print moveC,"is random intiger"
	S[moveC * 2] = order[turn]
	print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2
	Process()

def TWOMoveCPU(turn): # cpu move for turn 2
	if (S[1] or S[3] or S[5] or S[7]) == player:
		S[4] = order[turn]
		print "The Computer will go on space 5 index 4"
	if (S[0] or S[2] or S[6] or S[8]) == player:
		moveC = random.randint(0, 4)
		while S[moveC * 2] is not empty or moveC == 2:
			moveC = random.randint(0, 4)
		S[moveC * 2] = order[turn]
		print "The Computer will go on space",(moveC * 2) + 1,"index",moveC * 2
	if S[4] == player:
		if S[0] == cpu:
			S[8] = order[turn]
			print "The Computer will go on space 9 index 8"
		if S[2] == cpu:
			S[6] = order[turn]
			print "The Computer will go on space 7 index 6"
		if S[6] == cpu:
			S[2] = order[turn]
			print "The Computer will go on space 3 index 2"
		if S[8] == cpu:
			S[0] = order[turn]
			print "The Computer will go on space 1 index 0"
	Process()

def MoveCPU(turn): # cpu move for turns > 2
	global moveC, BlockFork
	BlockFork = []
	moveC = random.randint(0, 8)
	while S[moveC] is not empty:
		moveC = random.randint(0, 8)
	print moveC,"random move, placeholder"
	Restrict()
	print moveC,"Final Option for Move C"
	S[moveC] = order[turn]
	print "The Computer will go on space",moveC + 1,"index",moveC
	Process()

def Main(turn): # combines function into complete game
	Instructions()
	WhoGoesFirst()
	Process()
	while turn < 9: # gameplay in this loop
		print "turn:",turn + 1
		if order[turn] == player:
			MovePlayer(turn)
		if order[turn] == cpu:
			if turn == 0:
				ZEROMoveCPU(turn)
			if turn == 1:
				ONEMoveCPU(turn)
			if turn == 2:
				TWOMoveCPU(turn)
			if turn > 2:
				MoveCPU(turn)
		turn += 1
		if winner is not empty:
			turn = 9
			print winner + " Is tne Winner!\n"
		if winner is empty and turn == 9:
			print "The Game Is a Tie.\n"

Main(turn)

''' 
Issues
- Simplify CWin()
- Simplify CBlock()
- Simplify Letter()
- Simplify Main(turn)
'''
