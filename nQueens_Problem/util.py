"""
Some functions commonly used across the scripts
"""
import time

# check if the coordinate xy is under attack
# return boolean value
def is_attack(xy, qns):
    i = xy[0]; j = xy[1]
    for qn in qns:
        # print(qn)
        qn_i = qn[0]; qn_j = qn[1]
        # check if in same row or col
        if (qn_i == i) or (qn_j == j): return True
        # check if in diagonal
        if abs(qn_i - i) == abs(qn_j - j): return True
    return False

# edit grid to falsify cells that are under attack for i-th row
def check_row(row_i, grid, qns):
    for j in range(len(grid)):
        grid[row_i][j] = not is_attack([row_i, j], qns)
    return grid

# find the first feasible cell at i-th row for set up a queen
def get_qn(row_i, grid):
    for j in range(len(grid)):
        if grid[row_i][j] == True:
            return [row_i, j]
    return []

# check if the i-th row has any feasible cells
# return boolean value
def is_feasible_row(row_i, grid):
    for j in range(len(grid)):
        if grid[row_i][j] == True:
            return True
    return False

# lets check out the time complexity of the algo over number of queens
# expect to grow exponentially
def time_complexity(max_nqns, solve_func, **kwargs):
    nqns_arr, secs_arr = [], []
    for i in range(max_nqns):
        nqns = i + 1
        start = time.time()
        ans = solve_func(nqns, **kwargs)
        end = time.time()
        secs = (end - start)
        nqns_arr.append(nqns)
        secs_arr.append(secs_arr)
    return nqns_arr, secs_arr
