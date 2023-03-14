# Global variables
board = {}
turn = 'X'

# Will not work
def init_game():
	# Will not work because this creates a new variable
	# instead of assigning to the global board variable
	board = {
		'a1': None, `b1`: None, 'c1' None,
		# etc
	}
	turn = 'X'
   
# Do it like this
def init_game():
	# Use the global keyword to update global variables
	global board, turn
	board = {
		'a1': None, `b1`: None, 'c1' None,
		# etc
	}
	turn = 'X'