# Global variables
board = {}
turn = 'X'

   
# Do it like this
def init_game():
	# Use the global keyword to update global variables
	global board, turn
	board = {
		'a1': None, 'b1': None, 'c1' : None,
		'a2': None, 'b2': None, 'c2' : None,
		'a3': None, 'b3': None, 'c3' : None,
	}
	turn = 'X'