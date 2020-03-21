import numpy as np
from .Specie import Specie

def roullete_wheel(ps,haystack):
	"""
	returns a choosed needle from haystack based on roullete wheel selection
	"""
	random_number=np.random.random()
	_sum=0
	for p,needle in zip(ps,haystack):
		_sum+=p
		if random_number <= _sum:
			return needle

class Pool:
	def __init__(self,graph,popsize,crossover_rate,mutation_rate):
		
		self.graph=graph
		self.popsize=popsize
		self.crossover_rate=crossover_rate
		self.mutation_rate=mutation_rate

		self.gen=0
		dummy_genes=list(set(range(graph.n))-{self.graph.startindex})

		self.species=[]

		for _ in range(10):
			np.random.shuffle(dummy_genes)
			self.species.append(Specie(self.graph,list(dummy_genes)))
		self.best=None
		self.__update_ps()

	def __update_ps(self):
		sum_fitness=sum((specie.fitness for specie in self.species))
		self.ps=[specie.fitness/sum_fitness for specie in self.species]
		current_best=max(self.species)
		if self.best==None:
			self.best=current_best
		if current_best.fitness>self.best.fitness:
			self.best=current_best

	def __selection(self):
		next_species=[roullete_wheel(self.ps,self.species).copy() for _ in range(self.popsize)]
		self.species=next_species

	def __breed(self):
		for i,j in zip(range(0,self.popsize,2),range(1,self.popsize,2)):
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