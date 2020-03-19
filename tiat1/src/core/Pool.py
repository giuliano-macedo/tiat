import numpy as np
from .Specie import Specie
class Pool:
	def __init__(self,graph,popsize,crossover_rate,mutation_rate):
		
		self.graph=graph
		self.popsize=popsize
		self.crossover_rate=crossover_rate
		self.mutation_rate=mutation_rate

		self.gen=0
		dummy_genes=list(range(1,graph.n))

		self.species=[]

		for _ in range(10):
			np.random.shuffle(dummy_genes)
			self.species.append(Specie(self.graph,list(dummy_genes)))
		self.best=None
		self.__update_ps()

	def __update_ps(self):
		sum_fitness=sum((specie.fitness for specie in self.species))
		self.ps=[specie.fitness/sum_fitness for specie in self.species]
		_,best=max(((specie.fitness,specie) for specie in self.species),key=lambda t:t[0])
		if self.best==None:
			self.best=best
		if best.fitness>self.best.fitness:
			self.best=best

	def __selection(self):
		#roulette wheel selection
		next_species=[]
		for _ in range(self.popsize):
			_sum=0
			random_number=np.random.random()
			for specie,p in zip(self.species,self.ps):
				_sum+=p
				if random_number < _sum:
					next_species.append(specie.copy())
					break
		self.species=next_species

	def __breed(self):
		for i,j in zip(range(self.popsize),range(1,self.popsize)):
			if np.random.random() < self.crossover_rate:
				p1,p2=self.species[i],self.species[j]

				o1,o2=p1.crossover(p2)
				self.species[i]=o1
				self.species[j]=o2

	def __mutate(self):
		for specie in self.species:
			if np.random.random() < self.mutation_rate:
				specie.mutate()

	def step(self):
		#run a generation
		self.__selection()
		self.__breed()
		self.__mutate()
		self.__update_ps()
		self.gen+=1