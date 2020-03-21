
from numpy.random import randint

class Specie:
	def __init__(self,graph,genes,cache_fitness=True):
		self.graph=graph
		self.genes=genes
		self.cache_fitness=cache_fitness
		self.n=len(self.genes)
		if cache_fitness:
			self.fitness=self.compute_fitness()

	def __repr__(self):
		return f"Specie({repr(self.graph)},{repr(self.genes)})"

	def __lt__(self,other):
		if isinstance(other,Specie):
			return self.fitness<other.fitness
		return self.fitness<other.fitness

	def __fill_genes(self,genes,offspring,offspring_set,start=0):
		j=start
		for i in range(self.n):
			if offspring[i]!=None:continue
			while True:
				gene=genes[j]
				if gene in offspring_set:
					j=(j+1)%self.n
					continue
				offspring[i]=gene
				offspring_set.add(gene)
				j=(j+1)%self.n
				break

	def crossover(self,other,cut_points=None):
		if cut_points==None:
			mid=self.n//2
			first_point=randint(1,mid+1)
			second_point=randint(first_point+1,self.n)
			cut_points=first_point,second_point

		if len(cut_points)!=2:
			raise RuntimeError("invalid cut_points")
		
		l,h=cut_points
		
		o1=[None]*self.n
		o2=[None]*self.n
		o1_set=set()
		o2_set=set()


		#phase 1, preserve middle points

		o1[l:h]=self.genes [l:h]
		o2[l:h]=other.genes[l:h]
		o1_set|=set(self.genes [l:h])
		o2_set|=set(other.genes[l:h])

		#phase 2 fill genes
		self.__fill_genes(other.genes,o1,o1_set,
			# l-1
			0
		)
		self.__fill_genes(self.genes,o2,o2_set,
			# l-1
			0
		)

		return (
			Specie(self.graph,o1,self.cache_fitness),
			Specie(self.graph,o2,self.cache_fitness)
		)

	def compute_fitness(self):
		_set=set(self.genes)

		if len(_set)!=len(self.genes) or self.graph.startindex in _set:
			raise RuntimeError("invalid genes",self.genes)
		self.cost=self.graph.tsp_weight(self.genes)
		return 1/self.cost

	def mutate(self):
		#pair mutation
		pairs=set()
		while len(pairs)!=2:
			pairs.add(randint(self.n))
		i,j=pairs
		a,b=self.genes[i],self.genes[j]

		self.genes[i]=b
		self.genes[j]=a

	def copy(self):
		return Specie(self.graph,list(self.genes),self.cache_fitness)