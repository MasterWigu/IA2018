import sys
import ast
from pathlib import Path
from ia import *


def greedy_search(problem, h=None):
    """f(n) = h(n)"""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, h)

def xx_invalid_solution(board, result):
    board_result = result.state.board

    if not isinstance(result, Node):
        print("A procura devia retornar um objecto do tipo Node e nao um do tipo", type(result), "com valor", result)
        return True
    # Nao sei como chegar aqui
    # elif :
    #     state = result.state
    #     print("A accao", state.depth, "nao e valida", state.action, "A sequencia de accoes e:", state.solution())
    #     return True
    elif board_num_pegs(board_result) > 1:
        print("O tabuleiro nao tem só um pino:", board_result)
        return True

    return board == result.state.board


if len(sys.argv) == 2:
	arg_path = sys.argv[1]
else:
	arg_path = "tests_mooshak" #str(input('Insert path to mooshak_tests: '))

tests_home = Path(arg_path)
test_list = [x for x in tests_home.iterdir() if x.is_dir()]
test_list.sort()

for test_path in test_list:
	# Retrieving test contents
	test_name = str(test_path)[-6:]
	test_input_file  = open(str(test_path) + '/input', 'r')
	test_output_file = open(str(test_path) + '/output', 'r')

	test_input = test_input_file.read()
	test_output = test_output_file.read()

	test_input_file.close()
	test_output_file.close()

	# Running input content and comparing to its supposed output
	test_input = test_input[6:-2]
	test_input = eval(test_input)
	test_output = ast.literal_eval(test_output)

	print(test_name, "accepted" if test_input == test_output else "wrong")
