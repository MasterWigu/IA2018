import copy
from search import *

# TAI content
def c_peg ():
	return "O"
def c_empty ():
	return "_"
def c_blocked ():
	return "X"
def is_empty (e):
	return e == c_empty()
def is_peg (e):
	return e == c_peg()
def is_blocked (e):
	return e == c_blocked()


# TAI pos
# Tuplo (l, c)
def make_pos (l, c):
	return (l, c)
def pos_l (pos):
	return pos[0]
def pos_c (pos):
	return pos[1]

def valid_pos(pos):
	if (pos_l(pos) < 0 or pos_c(pos) < 0):
		return False
	return True

def lf_pos(pos):
	return make_pos(pos_l(pos), pos_c(pos)-1)
def rg_pos(pos):
	return make_pos(pos_l(pos), pos_c(pos)+1)
def up_pos(pos):
	return make_pos(pos_l(pos)-1, pos_c(pos))
def dn_pos(pos):
	return make_pos(pos_l(pos)+1, pos_c(pos))

# TAI move
# Lista [p_initial, p_final]
def make_move (i, f):
	return [i, f]
def move_initial (move):
	return move[0]
def move_final (move):
	return move[1]

def dif_move(move):
	return (pos_l(move_final(move))-pos_l(move_initial(move)), pos_c(move_final(move))-pos_c(move_initial(move)))


# TAI board
# Lista de listas
def board_size_l(board):
	return len(board)
def board_size_c(board):
	return len(board[0])
def board_pos_cont(board, pos):
	return board[pos_l(pos)][pos_c(pos)]
def board_chg_pos(board, pos, e):
	board[pos_l(pos)][pos_c(pos)] = e
def board_is_peg(board, pos):
	return is_peg(board_pos_cont(board, pos))
def board_is_empty(board, pos):
	return is_empty(board_pos_cont(board, pos))
def board_is_blocked(board, pos):
	return is_blocked(board_pos_cont(board, pos))


def board_moves(board):
	moves = []
	for i in range(board_size_l(board)-1):
		for j in range(board_size_c(board)-1):

			pos_i = make_pos(i,j)
			if board_is_peg(board, pos_i):
				if (board_is_peg(board, lf_pos(pos_i)) and board_is_empty(board, lf_pos(lf_pos(pos_i)))):
					if (valid_pos(lf_pos(lf_pos(pos_i)))):
						moves += [make_move(pos_i, lf_pos(lf_pos(pos_i)))]
				if (board_is_peg(board, rg_pos(pos_i)) and board_is_empty(board, rg_pos(rg_pos(pos_i)))):
					if (valid_pos(rg_pos(rg_pos(pos_i)))):
						moves += [make_move(pos_i, rg_pos(rg_pos(pos_i)))]
				if (board_is_peg(board, up_pos(pos_i)) and board_is_empty(board, up_pos(up_pos(pos_i)))):
					if (valid_pos(up_pos(up_pos(pos_i)))):
						moves += [make_move(pos_i, up_pos(up_pos(pos_i)))]
				if (board_is_peg(board, dn_pos(pos_i)) and board_is_empty(board, dn_pos(dn_pos(pos_i)))):
					if (valid_pos(dn_pos(dn_pos(pos_i)))):
						moves += [make_move(pos_i, dn_pos(dn_pos(pos_i)))]
	return moves


def board_perform_move(board, move):
	board_new = copy.deepcopy(board)
	diff = dif_move(move)

	board_chg_pos(board_new, move_initial(move), c_empty())
	board_chg_pos(board_new, move_final(move), c_peg())

	if (diff[0] == 0 and diff[1] > 0):
		board_chg_pos(board_new, rg_pos(move_initial(move)), c_empty())
	elif (diff[0] == 0 and diff[1] < 0):
		board_chg_pos(board_new, lf_pos(move_initial(move)), c_empty())
	elif (diff[1] == 0 and diff[0] > 0):
		board_chg_pos(board_new, dn_pos(move_initial(move)), c_empty())
	else:
		board_chg_pos(board_new, up_pos(move_initial(move)), c_empty())
	return board_new


def board_is_goal(board):
	if (board_num_pegs(board) <= 1):
		return True
	return False

def board_num_pegs(board):
	pegs = 0
	for i in range(board_size_l(board)-1):
		for j in range(board_size_c(board)-1):
			if (is_peg(board_pos_cont(board, make_pos(i,j)))):
				pegs+=1
	return pegs


def heuristic(board):
	dist = 0
	for i in range(board_size_l(board)-1):
		for j in range(board_size_c(board)-1):
			if (is_peg(board_pos_cont(board, make_pos(i,j)))):
				dist += distance(make_pos(i,j), (0,0))
	return dist



class sol_state:
	__slots__ = ['board']
	def __init__(self, board):
		self.board = board

	def __lt__(self, other_sol_state):
		return board_num_pegs(self.board) < board_num_pegs(other_sol_state.board)



class solitaire(Problem):
	"""Models a Solitaire problem as a satisfaction problem.
	A solution cannot have more than 1 peg left on the board."""
	def __init__(self, board):
		self.board = board

	def actions(self, state):
		return board_moves(state.board)


	def result(self, state, action):
		return board_perform_move(state.board, action)

	def goal_test(self, state):
		return board_is_goal(state.board)

	def path_cost(self, c, state1, action, state2):
		return c + 1
	
	def h(self, node):
		return heuristic(node.state.board)
