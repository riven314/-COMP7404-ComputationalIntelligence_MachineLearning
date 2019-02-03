#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:22:49 2019

Abstract:
Implement UCS(-GSA) algorithm using priority queue as data structure.
UCS = Uniform Cost Search. It explores the cheapest node first
*GSA will not explore repeated nodes, even though they are in the frontier

Extended Questions:
1. What would happen if we only consider smallest edge cost instead of accumulated cost

@author: Alex Lau
"""
from heapq import heappush, heappop

def UCS_GSA(graph_dict, start_node, end_node):
    frontier = []
    heappush(frontier, (0, start_node))
    explored_nodes = set()
    print('Initial frontier: ', list(frontier))
    # a pause
    input()
    while frontier:
        node = heappop(frontier)
        # we have reach the goal
        if (node[1].endswith(end_node)):
            return node
        # explore new node
        if node[1][-1] not in explored_nodes:
            print('Exploring: ', node[1][-1], 'at accumulated cost', node[0])
            explored_nodes.add(node[1][-1])
            for child in graph_dict[node[1][-1]]:
                # (accumulated cost, visited path)
                heappush(frontier, (node[0] + child[0], node[1] + child[1]))
            print(list(frontier))
            print(explored_nodes)
            input()


romania = {
'A':[(140,'S'),(118,'T'),(75,'Z')],'Z':[(75,'A'),(71,'O')],'O':[(151,'S'),(71,'Z')],
'T':[(118,'A'),(111,'L')],'L':[(70,'M'),(111,'T')],'M':[(75,'D'),(70,'L')],
'D':[(120,'C'),(75,'M')],'S':[(140,'A'),(99,'F'),(151,'O'),(80,'R')],
'R':[(146,'C'),(97,'P'),(80,'S')],'C':[(120,'D'),(138,'P'),(146,'R')],
'F':[(211,'B'),(99,'S')],'P':[(101,'B'),(138,'C'),(97,'R')],'B':[]}

eg = {
'S':[(10, 'G'),(3,'a'),(2,'d')],
'a':[(5,'b')], 
'b':[(2,'c'),(1,'e')],
'c':[(4,'G')],
'd':[(1,'b'),(4,'e')],
'e':[(3,'G')],
'G':[]
}

UCS_GSA(romania, 'A', 'B')
UCS_GSA(eg, 'S', 'G')