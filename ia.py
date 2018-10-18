import copy


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


class sol_state:
	def __init__(self, board):
     self.board = board

	def __lt__(self, other_sol_state):
		#cancro ask sarmento 

class solitaire(Problem):
 """Models a Solitaire problem as a satisfaction problem.
 A solution cannot have more than 1 peg left on the board."""
	def __init__(self, board):
 		"""The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.board = board

	def actions(self, state):
 	    """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""


	def result(self, state, action):
		"""Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""

	def goal_test(self, state):
		"""Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""


	def path_cost(self, c, state1, action, state2):
		"""Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

	def h(self, node):
 """Needed for informed search.""" 




b1 = [["_","O","O","O","_"], ["O","_","O","_","O"], ["_","O","_","O","_"], ["O","_","O","_","_"], ["_","O","_","_","_"]] 

print (board_moves(b1))

bn = board_perform_move(b1, [(0, 2), (0, 0)]) 

print (b1)
print('\n')
print  (bn)
