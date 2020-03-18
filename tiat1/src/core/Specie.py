#https://stackoverflow.com/a/312464/5133524

from numpy.random import randint

class Specie:
	def __init__(self,graph,genes):
		self.graph=graph
		self.genes=genes
		self.n=len(self.genes)

	def __repr__(self):
		return f"Specie({repr(self.graph)},{repr(self.genes)})"
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
			first_point=randint(1,mid)
			second_point=randint(mid,self.n)
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
		self.__fill_genes(other.genes,o1,o1_set,l-1)
		self.__fill_genes(self.genes,o2,o2_set,l-1)

		return Specie(self.graph,o1),Specie(self.graph,o2)


