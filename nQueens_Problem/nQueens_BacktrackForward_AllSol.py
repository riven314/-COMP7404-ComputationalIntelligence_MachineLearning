"""
Apply backtrack + forward checking to find all solutions of n-queens problem

Remarks:
1. for 8 queens, there are 92 unique solutions 
"""
from util import *

def solve(nqns):
	row_i = 0
	qns = []; qns_sets = []
	tmp = backtrack_all(nqns, row_i , qns, qns_sets)
	if len(qns_sets) == 0:
		print('No solution is found')
		return None
	else:
		return qns_sets

def backtrack_all(nqns, row_i, qns, qns_sets):
	#print(qns)
	#print(row_i)
	if row_i >= nqns:
		qns_sets.append(qns.copy())
		return False
	for j in range(nqns):
		if is_attack([row_i, j], qns):
			continue
		qns.append([row_i, j])
		if not backtrack_all(nqns, row_i+1, qns, qns_sets):
			rm_qn = qns.pop()
	return False

if __name__ == '__main__':
	nqns = int(input('Enter the number of queens: '))
	ans = solve(nqns)
	if ans is not None:
		print('Solutions found')
		print('There are ', len(ans), ' sets of solutions:')
		for i in ans:
			print(i)
	
