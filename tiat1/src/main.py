import argparse
import matplotlib.pyplot as plt
from itertools import permutations
from core import Graph,Specie,Pool
import numpy as np

def probabiliy(s):
	n=float(s)
	if not (0<=n<=100):
		raise RuntimeError("Value must be a probability in percentage")
	return n/100
def get_global_minimum(graph):
	initial=list(set(range(graph.n))-{graph.startindex})
	ans=max((Specie(graph,list(sol))) for sol in permutations(initial))
	print("best paths:")
	for sol in permutations(initial):
		specie=Specie(graph,list(sol))
		if specie.cost==ans.cost:
			specie.print()
	return ans
parser=argparse.ArgumentParser()
parser.add_argument("-p","--population_size",type=int,default=5)
parser.add_argument("-c","--crossover_rate",type=probabiliy,default=.65)
parser.add_argument("-m","--mutation_rate",type=probabiliy,default=.5)
parser.add_argument("-s","--seed",type=int,default=42)

args=parser.parse_args()

np.random.seed(args.seed)

graph=Graph("graph.json")

pool=Pool(
	graph,
	args.population_size,
	args.crossover_rate,
	args.mutation_rate
)
global_minimum=get_global_minimum(graph)
best_costs=[pool.best.cost]
while pool.best.cost!=global_minimum.cost:
	pool.step()
	best_costs.append(pool.best.cost)
print("path found:")
pool.best.print()

plt.plot(range(0,len(best_costs)),best_costs)
plt.xlabel("Generation")
plt.ylabel("Best Cost")
plt.title(f"population size={pool.popsize} crossover rate={pool.crossover_rate*100:.2g}% mutation rate={pool.mutation_rate*100:.2g}%")

plt.show()