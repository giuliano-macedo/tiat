import numpy as np
import random

class DE:
	def __init__(self,init_pop,fitness_callable,cr,f):
		self.pop=init_pop
		self.pop_size=len(self.pop)
		self.fitness=fitness_callable
		self.cr=cr
		self.f=f
		self.gen=0

	def step(self):
		new_pop=[]
		for x in self.pop:
			alpha,beta,gamma=random.sample(range(self.pop_size),3)

			v=self.pop[alpha] + (self.f*(self.pop[beta]-self.pop[gamma]))
			
			u=np.fromiter(( (vi if (random.random() <= self.cr) else xi) for xi,vi in zip(x,v)),np.float)
			
			new_pop.append(min([x,u],key=self.fitness))

		self.pop=new_pop
		self.gen+=1

	def pop_cost(self):
		return np.mean([self.fitness(x) for x in self.pop])