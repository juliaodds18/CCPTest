# TODO: Implement game of dice with human player and computer player

'''
Game is divided into rounds, where each player gets one turn 
Every turn, player rolls two six-sided dice
Winner: 
	- Highest double (if two doubles)
	- Double
	- Higher total (if no double)
	- Draw if same total 

Players switch turns between rounds
Computer winning average must be close to 70% 


The idea I had for this implementation was to allow the computer to throw multiple times if it knows it will lose. This can only be done during a round where human throws first, to maintain the illusion 
that the game is fair. If computer goes second, it knows the result of the human throw, and can therefore throw an additional number of times behind the scenes. 
To get the desired result of a ~70% winrate, I decided to tweak the number of times that the computer is allowed to perform additional throws. I found that allowing the computer to throw up to 8 
times allowed it to maintain a close to 70% winrate. It still appears fair, as the human does sometimes win when they go first, as the computer sometimes does not win even when allowed 7 additional throws,
so it is not too obvious that there is something going on behind the scenes. 
It should be mentioned that the way I interpereted the winrate discounts the number of draws, and only counts wins and losses. The winrate of the computer is therefore calculated as such 
	Computer winrate / Number of times a game resulted in a win for either party 
'''

from random import randint

# If lastTurn == 0, computer played first last round. If lastTurn == 1, human played first last round 
last_turn = 0

# Game controller, to ensure the game runs num_rounds times, as well as calculate the final scores
def game(num_rounds): 
	i = 0
	compWins = 0
	humanWins = 0
	draws = 0

	while i < num_rounds: 
		# Execute one round
		winner = round()

		# Print round results 
		print('Computer got: ' + str(winner[1]))
		print('Human got: ' + str(winner[2]))
		print('Winner: ' + winner[0])

		# Count who wins to calculate winrates
		i+= 1
		if (winner[0] == 'Computer wins'): 
			compWins+= 1
		elif winner[0] == 'Draw':
			draws += 1
		else:
			humanWins += 1
	
	return [compWins, humanWins, draws]
	

# Execute one round of the game
def round(): 
	#Determine whose turn it is 

	whose_turn()
	# Computer goes first
	if last_turn == 0:
		cpu_throw = dice_throw()
		human_throw = dice_throw()
		winner = determine_winner(cpu_throw, human_throw)
		win_info = [winner, cpu_throw, human_throw]
		return win_info

	# Human goes first
	else:
		human_throw = dice_throw()
		win_info = comp_cheats(human_throw)	
		return win_info


# Change turns 
def whose_turn(): 
	global last_turn
	if last_turn == 0: 
		last_turn = 1
	else:
		last_turn = 0


# Randomly throw die twice, returns a tuple of the result 
def dice_throw(): 
	throw = []
	throw.append(randint(1, 6))
	throw.append(randint(1, 6))
	return throw


# Ensures that computer gets the chance to throw multiple times to increase winrate
num_throws = 8
def comp_cheats(human_throw): 
	cpu_throw = []
	winner = ''
	i = 0

	# Allow computer to throw num_throws times in order to increase chance of winning
	while i < num_throws: 
		cpu_throw = dice_throw()
		winner = determine_winner(cpu_throw, human_throw)
		if (winner == 'Computer wins'): 
			break
		else:
			i+= 1
	return [winner, cpu_throw, human_throw]

# Determine who is the winner based on the ruleset described
def determine_winner(cpu_throw, human_throw):

	# Check if computer has double 
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

	# If we reach this code, then neither human nor computer have doubles, must calculate total to determine winner. Higher total wins
	else:
		cpu_total = cpu_throw[0] + cpu_throw[1]
		human_total = human_throw[0] + human_throw[1] 
		if cpu_total > human_total:
			return 'Computer wins'
		elif human_total > cpu_total:
			return 'Human wins'
		else:
			return 'Draw'



# Arbitrary number of rounds, set pretty high to get a good idea of the average winrates
num_rounds = 1000
game_info = game(num_rounds)
comp_wins = game_info[0]
human_wins = game_info[1]
draws = game_info[2]

# Print game results 
print('Computer wins: ' + str(comp_wins))
print('Human wins: ' + str(human_wins))
print('Draws: ' + str(draws))
print('Computer winrate: ' + str(float(comp_wins) / float(comp_wins + human_wins)))