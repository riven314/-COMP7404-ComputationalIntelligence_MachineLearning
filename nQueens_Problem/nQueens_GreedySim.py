#!/usr/bin/env python3
"""
Apply greedy algorithm on n queens problem. Initialize the configuration of n queens
and change the configuration if it leads to less number of attack. The algo does not garantee an optimal solution. Terminate if no smaller damage is found in next move.

Remark:
1. for tie smaller damage, arbitrary pick one step among those

To bo done:
1. using recurrence to update dmg from preceding dmg

Questions:
1. Avg. move to the solution
2. Probability of reaching an optimal solution

"""
from collections import defaultdict
from random import randint
import heapq

class nQueens:
	def __init__(self, nqns = None, qns = None):
		self.step = 0
		if qns is not None:
			self.nqns = len(qns)
			self.qns = qns
		if nqns is not None:
			self.nqns = nqns
			self.qns = self.init_qns()
		self.attacks = self.find_attacks()
		self.dmg = self.find_dmg()

	def solve(self, is_print = True):
		min_dmg, qns_pair = self.greedy_search()
		while min_dmg < self.dmg:
			self.step += 1
			add_qn = qns_pair[0]
			rm_qn = qns_pair[1]
			self.update_prop(add_qn, rm_qn)
			if is_print:
				print(self)
				input()
			min_dmg, qns_pair = self.greedy_search()	
		if self.dmg == 0:
			#print('global min is attained!')
			return self.qns
		else:
			#print('local min is attained!')
			return self.qns

	# greedy search for next step
	# return the best move for next step: dmg, add_qn and rm_qn
	def greedy_search(self):
		grid = []
		for i in range(self.nqns):
			for j in range(self.nqns):
				if (i, j) in self.qns:
					continue
				rm_qns = self.get_rm_qns((i, j))
				if rm_qns:
					add_qn = (i, j)
					min_ij = self.pseudo_update_prop(add_qn, rm_qns)
					heapq.heappush(grid, min_ij)
		min_dmg, qns_pair = heapq.heappop(grid)
		return min_dmg, qns_pair
	
	def get_rm_qns(self, add_qn):
		rm_qns = []
		for qn in self.qns:
			if self.is_attack(qn, add_qn): rm_qns.append(qn)
		return rm_qns	

	# calc the total dmg in the configuration
	def find_dmg(self):
		dmg = 0
		for node, adj_nodes in self.attacks.items():	
			dmg += len(adj_nodes)
		return int(dmg/2)
	
	# construct a graph with queens as node
	# edge is formed if 2 queens are under attack
	def find_attacks(self):
		attacks = defaultdict(set)
		for qn1 in self.qns:
			attacks[qn1] = set()
			for qn2 in self.qns:
				if self.is_attack(qn1, qn2): attacks[qn1].add(qn2)
		return attacks		
	
	# check if 2 queens are attacking each other
	def is_attack(self, qn1, qn2):
		if qn1 == qn2:
			return False
		if qn1[0] == qn2[0]:
			return True
		if qn1[1] == qn2[1]:
			return True
		if abs(qn1[0] - qn2[0]) == abs(qn1[1] - qn2[1]):
			return True
		return False
	
	# create a dummy class to avoid in-place update of this object properties
	def pseudo_update_prop(self, add_qn, rm_qns):
		ij_dmg = float("inf")
		ij_qns = None
		for rm_qn in rm_qns:
			# avoid inplace change in self.qns
			qns_copy = self.qns.copy()
			tmp_c = nQueens(qns = qns_copy)
			tmp_c.update_prop(add_qn, rm_qn)
			tmp_dmg = tmp_c.dmg
			if tmp_dmg < ij_dmg:
				ij_dmg = tmp_dmg
				ij_qns = ((add_qn, rm_qn))
		return ij_dmg, ij_qns
	
	# can apply recurrence to update attacks and dmg
	def update_prop(self, add_qn, rm_qn):	
		# update qns
		self.qns.remove(rm_qn)
		self.qns.add(add_qn)
		# update attacks
		tmp = self.attacks.pop(rm_qn)
		for qn in self.qns:
			if qn == add_qn:
				continue
			if rm_qn in self.attacks[qn]:
				self.attacks[qn].remove(rm_qn)
			if self.is_attack(qn, add_qn):
				self.attacks[add_qn].add(qn)
				self.attacks[qn].add(add_qn)	
		# update dmg
		self.dmg = self.find_dmg()
		pass
	
	# init all queens
	def init_qns(self):
		qns = set()
		while len(qns) != self.nqns:
			qn = self.init_qn()
			if qn not in qns: qns.add(qn)
		return qns
	
	# create a queen
	def init_qn(self):
		end_pt = self.nqns - 1
		x, y = randint(0, end_pt), randint(0, end_pt)
		return (x, y)
	
	# print the grid with queens locations
	def __str__(self):
		print('[Step %d] Damage = %d \n' % (self.step, self.dmg))
		for i in range(self.nqns):
			for j in range(self.nqns):
				print('_ ', end = '') if (i,j) not in self.qns else print('Q ', end = '')
			print('\n')
		return ''

if __name__ == "__main__":
	print('Lets calculate the prob of greedy algo reaching global min...')
	nqns = int(input('Enter the number of queens: '))
	nsim = int(input('Enter the number of simulations: '))
	print('Simulation start...')
	steps = []
	cnt = 0
	dmgs = []
	for i in range(nsim):
		tmp = nQueens(nqns = nqns)
		x = tmp.solve(is_print = False)
		steps.append(tmp.step)
		dmgs.append(tmp.dmg)
		if tmp.dmg == 0:
			cnt += 1
	prb = round((cnt/nsim)*100, 4)
	avg_step = sum(steps)/nsim
	avg_dmg = sum(dmgs)/nsim
	print('Simulation completed.')
	print('Prob = ', prb, '%')
	print('Expected Steps = ', avg_step)
	print('Expected Cost = ', avg_dmg)
