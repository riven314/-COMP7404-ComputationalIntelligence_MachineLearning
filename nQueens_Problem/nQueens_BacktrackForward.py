"""
Implement backtracking + forward checking algorithm on n-queens problem by iterative method
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
from util import *

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

if __name__ == "__main__":
	nqns = int(input('Enter the number of queens: '))
	qns = solve(nqns)
	print('The solution is: ')
	print(qns)

