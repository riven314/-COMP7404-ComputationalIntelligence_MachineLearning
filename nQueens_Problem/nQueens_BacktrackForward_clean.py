"""
Reference from solution by Geeksforgeeks
apply backtracking + forward checking on n queens problem
"""
import resource, sys
from util import *

def solve(nqns, max_depth = None):
	if max_depth is not None:
		sys.setrecursionlimit(max_depth)
	grid = [[0 for i in range(nqns)] for j in range(nqns)]
	qns = []
	if backtrack(grid, 0, qns):
		return qns
	else:
		print('No solution is found')
		return None

def backtrack(grid, row_i, qns):
	n = len(grid)
	if len(qns) == n:
		return True
	for j in range(n):
		if is_attack([row_i,j], qns):
			continue
		# place the queen if it is safe
		grid[row_i][j] = 1
		qns.append([row_i,j])
		if backtrack(grid, row_i+1, qns):
			return True
		# remove the latest queen no feasible sol for next row
		grid[row_i][j] = 0
		rm_qn = qns.pop()
	return False

if __name__ == '__main__':
	nqns = int(input('Enter the number of queens: '))
	qns = solve(nqns)
	print('The solution is: ')
	print(qns)

