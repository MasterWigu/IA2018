#Catarina Pedreira - 87524 / Miguel Oliveira - 87689

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

def valid_pos(board, pos):
	if (pos_l(pos) >= 0 and pos_c(pos) >= 0 and pos_l(pos)< board_size_l(board) and pos_c(pos) < board_size_c(board)):
		return True
	return False

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
	return make_pos(pos_l(move_final(move))-pos_l(move_initial(move)), pos_c(move_final(move))-pos_c(move_initial(move)))


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
	for i in range(board_size_l(board)):
		for j in range(board_size_c(board)):

			pos_i = make_pos(i,j)
			if board_is_peg(board, pos_i):
				if (valid_pos(board, lf_pos(lf_pos(pos_i)))):
					if (board_is_peg(board, lf_pos(pos_i)) and board_is_empty(board, lf_pos(lf_pos(pos_i)))):
						moves += [make_move(pos_i, lf_pos(lf_pos(pos_i)))]
				if (valid_pos(board, rg_pos(rg_pos(pos_i)))):
					if (board_is_peg(board, rg_pos(pos_i)) and board_is_empty(board, rg_pos(rg_pos(pos_i)))):
						moves += [make_move(pos_i, rg_pos(rg_pos(pos_i)))]
				if (valid_pos(board, up_pos(up_pos(pos_i)))):
					if (board_is_peg(board, up_pos(pos_i)) and board_is_empty(board, up_pos(up_pos(pos_i)))):
						moves += [make_move(pos_i, up_pos(up_pos(pos_i)))]
				if (valid_pos(board, dn_pos(dn_pos(pos_i)))):
					if (board_is_peg(board, dn_pos(pos_i)) and board_is_empty(board, dn_pos(dn_pos(pos_i)))):
						moves += [make_move(pos_i, dn_pos(dn_pos(pos_i)))]
	return moves


def board_perform_move(board, move):
	board_new = copy.deepcopy(board)
	diff = dif_move(move)

	board_chg_pos(board_new, move_initial(move), c_empty())
	board_chg_pos(board_new, move_final(move), c_peg())

	if (pos_l(diff) == 0 and pos_c(diff) > 0):
		board_chg_pos(board_new, rg_pos(move_initial(move)), c_empty())
	elif (pos_l(diff) == 0 and pos_c(diff) < 0):
		board_chg_pos(board_new, lf_pos(move_initial(move)), c_empty())
	elif (pos_c(diff) == 0 and pos_l(diff) > 0):
		board_chg_pos(board_new, dn_pos(move_initial(move)), c_empty())
	else:
		board_chg_pos(board_new, up_pos(move_initial(move)), c_empty())
	return board_new


def board_is_goal(state):
	if (state.numPegs == 1):
		return True
	return False

def board_num_pegs(board):
	pegs = 0
	for i in range(board_size_l(board)):
		for j in range(board_size_c(board)):
			if (is_peg(board_pos_cont(board, make_pos(i,j)))):
				pegs+=1
	return pegs

def heuristic(state):
	moves = board_moves(state.board)

	pegs_move = []
	for i in moves:
		pegs_move.append(move_initial(i))

	numPegsMove = len(set(pegs_move))

	return state.numPegs + (state.numPegs - numPegsMove)


class sol_state:
	def __init__(self, board, pegs = -1):
		if (pegs == -1):
			self.numPegs = board_num_pegs(board)
		else:
			self.numPegs = pegs
		self.board = board

	def __lt__(self, other_sol_state):
		return self.numPegs > other_sol_state.numPegs




class solitaire(Problem):
	def __init__(self, board):
		self.initial = sol_state(board, board_num_pegs(board))

	def actions(self, state):
		return board_moves(state.board)


	def result(self, state, action):
		return sol_state(board_perform_move(state.board, action), state.numPegs - 1)

	def goal_test(self, state):
		if (state.numPegs == 1):
			return True
		return False

	def path_cost(self, c, state1, action, state2):
		return c + 1
	
	def h(self, node):
		return heuristic(node.state)
