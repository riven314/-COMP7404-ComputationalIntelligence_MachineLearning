"""
Log: 
1. Try iterative approach, but fail because it can only save one infeasible location.
Should save all the infeasible locations. 


"""
# n_qn: number of queens
def solve(n_qn):
	row_i = 0
	row = [True for i in range(n_qn)]
	qns = []
	backtrack(row_i, row, qns)
	return qns

# apply backtrack algo by recursion
def backtrack(row_i, row, qns):
	next_row = [True for i in range(len(row))]
	next_row_i = row_i + 1
	# go one level down if feasible solution is found
	if is_feasible_row(next_row_i, next_row, qns):
		if not len(qns) == len(row):
			backtrack(next_row_i, row, qns)
	# go one level back if no feasible solution is found
	else:
		rm_qn = qns.pop()
		print('remove: ', rm_qn, ' at row ', row_i)
		row[rm_qn[1]] = False
		backtrack(row_i, row, qns)

# up qns and row at i-th index and return boolean
def is_feasible_row(row_i, row, qns):
	row = check_row(row_i, row, qns)
	qn = get_qn(row_i, row)
	if not qn:
		return False
	qns.append(qn)
	return True

row = [True for i in range(4)]
qns = [[0,0]]

# check if the queen is under attack if it is in the coordinate [x,y]
def is_attack(xy, qns):
	# corner case
	if len(qns) == 0:
		return True
	i = xy[0]; j = xy[1]
	for qn in qns:
		qn_i = qn[0]
		qn_j = qn[1]
		# chekc if in same row or column
		if (qn_i == i) or (qn_j == j):
			return False
		# check if in diagonal line
		if abs(qn_i - i) == abs(qn_j - j):
			return False
	return True


# for the i-throw, given the preceding queens location
# identify location that is under attack
def check_row(row_i, row, qns):
	for j in range(len(row)):
		xy = [row_i, j]
		row[j] = is_attack(xy, qns)
	return row


# find the first feasible location at i-th row
def get_qn(row_i, row):
	for j in range(len(row)):
		if row[j] == True:
			return [row_i, j]
	return []
