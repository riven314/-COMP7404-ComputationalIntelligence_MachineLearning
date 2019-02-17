"""
Apply backtrack + AC-3(arc consistency-3) on color mapping problem

design:
1. construct a class to store a constraint satisfaction problem, it contains:
    > a mapping between variables and value
    > a graph specifying the dependency between variables
    > constraint function returning boolean value (make it generic)
    > domains for each variable
    > a function to get list of (distinct) arcs from the graph
2. backtrack is done in recursion and randomly pick a variable for assignment
3. arc consistency is for checking the early failure

notes:
1. during arc consistency checking, csp object will be changed

"""
import collections
from copy import deepcopy

class csp:
    """class for constraint satisfaction problem

    properties
    vars -- dict of vars with value assigned
    domains -- dict of sets, key being var and value being its domain
    graph -- dict of list showing dependency of variables

    methods
    get_arcs -- get list of distinct arcs
    constraint_func -- return boolean to see if two values are the same
    """
    def __init__(self, vars, domains, graph):
        self.vars = vars
        self.domains = domains
        self.graph = graph

    def get_arcs(self):
        arcs = [(vi, vj) for vi in self.graph.keys() for vj in graph[vi]]
        arcs += [(vj, vi) for vi, vj in arcs]
        return arcs
    
    def constraint_func(self, x, y):
        if x == y:
            return False
        else:
            return True
    
    def next_var(self):
        """
        return the var that is first detected to be None
        """
        for v, x in self.vars.items():
            if x is None:
                return v
        return None

def backtrack(csp):
    # select a variable randomly
    next_v = csp.next_var()
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
    print(arcs_queue)
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
    print('[from] ', vi, csp.domains[vi])
    print('[to] ', vj, csp.domains[vj])
    print('remove from ', vi, ': ', rm_vals) 
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
    #print(backtrack(csp_obj))

