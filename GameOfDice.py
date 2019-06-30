# TODO: Implement game of dice with human player and computer player

# Game is divided into rounds, where each player gets one turn 
# Every turn, player rolls two six-sided dice
# Winner: 
	# Highest double (if two doubles)
	# Double
	# Higher total (if no double)
	# Draw if same total 

# Players switch turns between rounds

# Computer winning average must be close to 70% 

from random import randint

# If lastTurn == 0, computer played first last round. If lastTurn == 1, human played first last round 
last_turn = 0

def game(): 
	while True: 
		winner = round()
		print(winner)

def round(): 
	#Determine who'se turn it is 

	whose_turn()
	# Computer goes first
	if last_turn == 0:
		# Computer goes first
		cpu_throw = dice_throw()
		human_throw = dice_throw()
		winner = determine_winner(cpu_throw, human_throw)
		return winner

	# Human goes first
	else:
		human_throw = dice_throw()
		cpu_throw = dice_throw()
		winner = determine_winner(cpu_throw, human_throw)		
		return winner


def whose_turn(): 
	global last_turn
	if last_turn == 0: 
		last_turn = 1
	else:
		last_turn = 0




def dice_throw(): 
	throw = []
	throw.append(randint(1, 6))
	throw.append(randint(1, 6))
	return throw



def determine_winner(cpu_throw, human_throw):
	# Check if computer has double 
	print(cpu_throw)
	print(human_throw)
	if (cpu_throw[0] == cpu_throw[1]):	
		# Check if human has double as well 
		if (human_throw[0] == human_throw[1]): 

			# Find who has a higher double. If even, then it's a draw
			if (cpu_throw[0] > human_throw[0]): 
				return 'Computer wins'
			elif (human_throw[0] > cpu_throw[0]):
				return 'Human wins'
			else: 
				return 'Draw'
		else: 
			return 'Computer wins'
	# Check if human has double
	elif (human_throw[0] == human_throw[1]): 
		# Have already checked if computer has a double 
		# So if we have reached this code, computer does not have double, human wins
		return 'Human wins'

	# If we reach this code, then neither human nor computer have doubles, must calculate total to determine winner
	else:
		cpu_total = cpu_throw[0] + cpu_throw[1]
		human_total = human_throw[0] + human_throw[1] 
		if cpu_total > human_total:
			return 'Computer wins'
		elif human_total > cpu_total:
			return 'Human wins'
		else:
			return 'Draw'



game()