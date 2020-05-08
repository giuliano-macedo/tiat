import numpy as np
import random

class DE:
	def __init__(self,init_pop,fitness_callable,cr,f):
		self.pop=init_pop
		self.fitness=fitness_callable
		self.cr=cr
		self.f=f
		self.gen=0

	def step(self):
		new_pop=[]
		for i in self.pop:
			alpha,beta,gamma=random.sample(range(len(self.pop)),3)
			
			x=self.pop[alpha]
			v=self.pop[alpha] - (self.f*(self.pop[beta]-self.pop[gamma]))
			u=np.zeros((len(v)))
			
			for i,(xj,vj) in enumerate(zip(x,v)):
				rand=random.random()
				u[i]=vj if rand <= self.cr else xj

			new_pop.append(min([x,u],key=self.fitness))
		
		self.pop=new_pop
		self.gen+=1

	def pop_cost(self):
		return np.mean([self.fitness(x) for x in self.pop])