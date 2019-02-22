"""
1. construct a class to store a constraint satisfaction problem, it contains:
    > a mapping between variables and value
    > a graph specifying the dependency between variables
    > constraint function returning boolean value (make it generic)
    > domains for each variable
    > map of var to its node degree
    > a function to get list of (distinct) arcs from the graph

"""
import heapq

class csp:
    """class for constraint satisfaction problem

    properties
    vars -- dict of vars with value assigned
    domains -- dict of sets, key being var and value being its domain
    graph -- dict of list showing dependency of variables
    degree -- tuple (var, node degree of var), negative extract min 

    methods
    get_arcs -- get list of distinct arcs
    constraint_func -- return boolean to see if two values are the same
    """ 
    def __init__(self, vars, domains, graph):
        self.vars = vars
        self.domains = domains
        self.graph = graph
        self.degree = self.get_degree()

    def get_degree(self):
        degree_heap = [(-1 * len(self.graph[var]), var) for var, _ in self.vars.items()]
        heapq.heapify(degree_heap)
        return degree_heap

    def get_arcs(self):
        arcs = [(vi, vj) for vi in self.graph.keys() for vj in self.graph[vi]]
        arcs += [(vj, vi) for vi, vj in arcs]
        return arcs
        
    def constraint_func(self, x, y): 
        if x == y:
            return False
        else:
            return True
    
    def next_var_bydegree(self):
        """ 
        return the var that is None and have largest degree
        """ 
        while self.degree:
            _, var = heapq.heappop(self.degree)
            if self.vars[var] is None:
               return var 
        return None

    def next_var_naive(self):
        """ 
        return the var that is the first occurence of None
        """ 
        for var, x in self.vars.items():
            if x is None:
                return var 
        return None

