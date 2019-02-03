"""
Implement backtracking algorithm on n-queens problem by iterative method
using 2D array to represent a grid

Remark:
1. For time complexity, it is exponential
2. For space complexity, it can be reduce from O(n^2) to O(n)
3. Relax the recursion depth to allow higher number of n_qn (n_qn >= 13)

Reference:
1. relax recursion limit https://stackoverflow.com/questions/3323001/what-is-the-maximum-recursion-depth-in-python-and-how-to-increase-it
2. 
"""
import resource, sys
import time

# lets check out the time complexity of the algo over number of queens
# expect to grow exponentially
def time_complexity(max_nqns, max_depth):
	nqns_arr, secs_arr = [], []
	for i in range(max_nqns):
		nqns = i + 1
		start = time.time()
		ans = solve(nqns, max_depth = max_depth)
		end = time.time()
		secs = (end - start)
		nqns_arr.append(nqns)
		secs_arr.append(secs_arr)
	return nqns_arr, secs_arr		

# main solver
def solve(n_qn, max_depth = None):
	if max_depth is not None:
		#resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
		sys.setrecursionlimit(max_depth)
	row_i = 0
	grid = [[True for i in range(n_qn)] for j in range(n_qn)]
	qns = []
	backtrack_2d(row_i, grid, qns)
	return qns

# the recursive make change on the input var in place
# output none
def backtrack_2d(row_i, grid, qns):
	# print('row idx: ', row_i, ' | qns: ', qns)
	if len(qns) == len(grid):
		return None
	# identify infeasible cells at i-th row
	grid = check_row(row_i, grid, qns)
	# track preceding row if no feasible cells are found
	while not is_feasible_row(row_i, grid):
		if row_i == 0:
			print('There is no solution')
			qns = []
			return None
		else:
			row_i -= 1
			rm_qn_i, rm_qn_j = qns.pop()
			grid[rm_qn_i][rm_qn_j] = False
	# else go ahead to next row
	qn = get_qn(row_i, grid)
	qns.append(qn)
	row_i += 1
	backtrack_2d(row_i, grid, qns)

# check if the i-th row has any feasible cells
# return boolean value
def is_feasible_row(row_i, grid):
	for j in range(len(grid)):
		if grid[row_i][j] == True:
			return True
	return False

# check if the coordinate xy is under attack
# return boolean value
def is_attack(xy, qns):
	i = xy[0]; j = xy[1]
	for qn in qns:
		# print(qn)
		qn_i = qn[0]; qn_j = qn[1]
		# check if in same row or col
		if (qn_i == i) or (qn_j == j):
			return False
		# check if in diagonal
		if abs(qn_i - i) == abs(qn_j - j):
			return False
	return True

# edit grid to falsify cells that are under attack for i-th row
def check_row(row_i, grid, qns):
	for j in range(len(grid)):
		grid[row_i][j] = is_attack([row_i, j], qns)
	return grid

# find the first feasible cell at i-th row for set up a queen
def get_qn(row_i, grid):
	for j in range(len(grid)):
		if grid[row_i][j] == True:
			return [row_i, j]
	return []


