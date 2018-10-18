from ia import *



print('TESTE 1\n')
result1 = str(sorted(board_moves([["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])))
if (result1 == '[[(0, 2), (0, 0)], [(0, 2), (0, 4)], [(0, 2), (2, 2)]]'):
	print('TESTE 1 CORRECTO\n')
else:
	print('TESTE 1 ERRADO\n')



print('TESTE 3\n')
result1 = str(sorted(board_moves([["_","O","O","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])))
if (result1 == '[[(0, 2), (0, 0)], [(0, 2), (0, 4)], [(0, 2), (2, 2)], [(1, 3), (1, 1)], [(1, 3), (3, 3)]]'):
	print('TESTE 3 CORRECTO\n')
else:
	print('TESTE 3 ERRADO\n')


print('TESTE 5\n')
result1 = str(sorted(board_moves([["O","O","_","X","X","X"],["O","_","O","O","O","O"],["_","O","O","_","O","O"],["O","O","O","_","O","O"]])))
if (result1 == '[[(0, 0), (0, 2)], [(0, 0), (2, 0)], [(1, 3), (1, 1)], [(2, 1), (2, 3)], [(2, 2), (0, 2)], [(2, 2), (2, 0)], [(2, 5), (2, 3)], [(3, 1), (1, 1)], [(3, 1), (3, 3)], [(3, 5), (3, 3)]]'):
	print('TESTE 5 CORRECTO\n')
else:
	print('TESTE 5 ERRADO\n')


print('TESTE 7\n')
result1 = str(sorted(board_moves([["O","O","_","X","X","X"],["O","_","O","O","O","O"],["_","O","O","_","O","O"],["O","O","_","X","X","X"]])))
if (result1 == '[[(0, 0), (0, 2)], [(0, 0), (2, 0)], [(1, 2), (3, 2)], [(1, 3), (1, 1)], [(2, 1), (2, 3)], [(2, 2), (0, 2)], [(2, 2), (2, 0)], [(2, 5), (2, 3)], [(3, 0), (3, 2)], [(3, 1), (1, 1)]]'):
	print('TESTE 7 CORRECTO\n')
else:
	print('TESTE 7 ERRADO\n')



print('TESTE 9\n')
result1 = str(board_perform_move([["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]], [(0, 2), (0, 0)]))
if (result1 == "[['O', '_', '_', 'O', '_'], ['O', '_', 'O', '_', 'O'], ['_', 'O', '_', 'O', '_'], ['O', '_', 'O', '_', '_'], ['_', 'O', '_', '_', '_']]"):
	print('TESTE 9 CORRECTO\n')
else:
	print('TESTE 9 ERRADO\n')



print('TESTE 11\n')
result1 = str(board_perform_move([["_","O","O","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]], [(1, 3), (1, 1)]))
if (result1 == "[['_', 'O', 'O', 'O', '_'], ['O', 'O', '_', '_', 'O'], ['_', 'O', '_', 'O', '_'], ['O', '_', 'O', '_', '_'], ['_', 'O', '_', '_', '_']]"):
	print('TESTE 11 CORRECTO\n')
else:
	print('TESTE 11 ERRADO\n')



print('TESTE 13\n')
result1 = str(type(sol_state([["_","O","O","O","_"],["O","_","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])) is sol_state)
if (result1 == "True"):
	print('TESTE 13 CORRECTO\n')
else:
	print('TESTE 13 ERRADO\n')


print('TESTE 15\n')
result1 = str(sol_state([["_","O","O","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]])>sol_state([["_","O","_","O","_"],["O","_","O","O","O"],["_","O","_","O","_"],["O","_","O","_","_"],["_","O","_","_","_"]]))
if (result1 == "False"):
	print('TESTE 15 CORRECTO\n')
else:
	print('TESTE 15 ERRADO\n')


print('TESTE 17\n')
result1 = str(type(solitaire([["X","O","O","O","X"],["O","O","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["X","O","_","_","X"]])) is solitaire)
if (result1 == "True"):
	print('TESTE 17 CORRECTO\n')
else:
	print('TESTE 17 ERRADO\n')



print('TESTE 19\n')
result1 = str(solitaire([["X","O","O","O","X"],["O","O","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["X","O","_","_","X"]]).initial.board)
if (result1 == "[['X', 'O', 'O', 'O', 'X'], ['O', 'O', 'O', '_', 'O'], ['_', 'O', '_', 'O', '_'], ['O', '_', 'O', '_', '_'], ['X', 'O', '_', '_', 'X']]"):
	print('TESTE 19 CORRECTO\n')
else:
	print('TESTE 19 ERRADO\n')


print('TESTE 21\n')
result1 = str(sorted(solitaire([["X","O","O","O","X"],["O","O","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["X","O","_","_","X"]]).actions(sol_state([["X","O","O","O","X"],["O","O","O","_","O"],["_","O","_","O","_"],["O","_","O","_","_"],["X","O","_","_","X"]]))))
if (result1 == "[[(0, 2), (2, 2)], [(1, 1), (1, 3)], [(1, 1), (3, 1)]]"):
	print('TESTE 21 CORRECTO\n')
else:
	print('TESTE 21 ERRADO\n')


print('TESTE 22\n')
result1 = str(solitaire([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]).goal_test(sol_state([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]])))
if (result1 == "False"):
	print('TESTE 22 CORRECTO\n')
else:
	print('TESTE 22 ERRADO\n')



print('TESTE 25\n')
result1 = str(solitaire([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]).result(sol_state([["X","O","_","O","X"],["O","_","_","_","O"],["_","_","_","_","O"],["O","O","_","_","O"],["X","O","O","O","X"]]),[(3, 0), (3, 2)]).board)
if (result1 == "[['X', 'O', '_', 'O', 'X'], ['O', '_', '_', '_', 'O'], ['_', '_', '_', '_', 'O'], ['_', '_', 'O', '_', 'O'], ['X', 'O', 'O', 'O', 'X']]"):
	print('TESTE 25 CORRECTO\n')
else:
	print('TESTE 25 ERRADO\n')




