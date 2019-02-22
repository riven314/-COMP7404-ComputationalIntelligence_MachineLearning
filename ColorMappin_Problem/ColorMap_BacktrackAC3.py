"""
Apply backtrack + AC-3(arc consistency-3) + Variable Selection on color mapping problem

design:
1. backtrack is done in recursion and randomly pick a variable for assignment
2. arc consistency is for checking the early failure

notes:
1. during arc consistency checking, csp object will be changed

"""
import collections
from copy import deepcopy
from CspClass import *

def backtrack(csp):
    # select a variable randomly
    next_v = csp.next_var_bydegree()
    print('%s is selected' % next_v)
    # complete the loop if all var is assigned a valid value
    if next_v is None:
        return True
    # backup domains 
    csp_cp = deepcopy(csp)
    for x in csp.domains[next_v].copy():
        csp.vars[next_v] = x
        # pass to next recursion
        if is_arc_consistent(csp):
            if backtrack(csp):
                return True
        # undo the updates
        csp = csp_cp
    return False

def is_arc_consistent(csp):
    # if the var is not None, set its domain to be the var itself 
    # v: variable. x: value of the variable
    for v, x in csp.vars.items():
        if x is not None: csp.domains[v] = {x}
    # get all distinct arcs i.e (vi, vj) != (vj, vi)
    arcs_queue = collections.deque(csp.get_arcs())
    #print(arcs_queue)
    while arcs_queue:
        vi, vj = arcs_queue.popleft()
        if is_revise(csp, vi, vj):
            if len(csp.domains[vi]) == 0: 
                return False
            for vk in csp.graph[vi]:
                if vk == vj:
                   continue
                arcs_queue.append((vk, vi))
    return True

# check if there is any change in domains
def is_revise(csp, vi, vj):
    revised = False
    rm_vals = set()
    for x in csp.domains[vi]:
        if not is_map(csp, x, csp.domains[vj]):
            rm_vals.add(x)
            revised = True
    #print('[from] ', vi, csp.domains[vi])
    #print('[to] ', vj, csp.domains[vj])
    #print('remove from ', vi, ': ', rm_vals) 
    # remove all invalid values in vi's domain
    csp.domains[vi] -= rm_vals
    return revised

# for element x, check if there is any element in domain that can satisfy the constraint
def is_map(csp, x, domain):
    mapped = False
    for y in domain:
        if csp.constraint_func(x, y):
            mapped = True
    return mapped

if __name__ == '__main__':
    #vars = {'NT': 'G', 'WA': 'R', 'NSW': 'R',
    #        'SA': None, 'Q': None, 'V': None}
    vars = {'NT': None, 'WA': None, 'NSW': None,
            'SA': None, 'Q': None, 'V': None,
            'T': None}
    graph = {'WA': ['NT', 'SA'],
            'NT': ['WA', 'SA', 'Q'],
            'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
            'Q': ['NT', 'SA', 'NSW'],
            'NSW': ['Q', 'SA', 'V'],
            'V': ['SA', 'NSW'],
            'T': []}
    domain = {'R', 'B', 'G'}
    domains = {var: domain.copy() for var in vars.keys()}
    csp_obj = csp(vars, domains, graph)
    #print(is_arc_consistent(csp_obj))
    print(backtrack(csp_obj))

